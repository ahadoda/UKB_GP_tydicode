from __future__ import annotations

import unittest
from pathlib import Path
import re

import pandas as pd

from src.trait_codelists import load_codelist, load_manifest, match_codes


class TraitCodelistTests(unittest.TestCase):
    def test_manifest_contains_measurements_and_medications(self) -> None:
        manifest = load_manifest()
        self.assertIn("body_mass_index", set(manifest["trait"]))
        self.assertIn("hba1c", set(manifest["trait"]))
        self.assertIn("tsh", set(manifest["trait"]))
        self.assertIn("red_cell_distribution_width", set(manifest["trait"]))
        self.assertIn("lipid_lowering", set(manifest["trait"]))

    def test_scope_contains_complete_phenoage_marker_set(self) -> None:
        scope = pd.read_csv("catalogue/biomarker_scope.csv")
        phenoage = set(
            scope.loc[scope["biological_age_role"].eq("PhenoAge"), "biomarker"]
        )
        self.assertEqual(
            phenoage,
            {
                "albumin",
                "alkaline phosphatase",
                "creatinine",
                "glucose",
                "C-reactive protein",
                "lymphocyte percentage",
                "mean corpuscular volume",
                "red cell distribution width",
                "white blood cell count",
            },
        )

    def test_public_codelists_are_simple_and_final(self) -> None:
        index = pd.read_csv("phenotypes/index.csv")
        self.assertEqual(len(index), 97)
        hba1c = pd.read_csv(
            "phenotypes/glycaemia/gp_read2_hba1c.txt",
            sep="\t",
            dtype="string",
            comment="#",
        )
        self.assertEqual(
            hba1c.columns.tolist(),
            ["code", "description", "code_group", "recommended_use"],
        )
        self.assertNotIn("selection_tier", hba1c.columns)
        self.assertTrue(hba1c["code_group"].str.len().gt(0).all())
        self.assertTrue(hba1c["recommended_use"].str.len().gt(0).all())
        public_text = Path(
            "phenotypes/glycaemia/gp_read2_hba1c.txt"
        ).read_text(encoding="utf-8")
        self.assertIn("# DCCT-aligned HbA1c", public_text)

    def test_public_guidance_distinguishes_context_and_literal_dots(self):
        glucose = pd.read_csv(
            "phenotypes/glycaemia/gp_read2_blood_glucose.txt",
            sep="\t",
            dtype="string",
            comment="#",
        )
        fasting = glucose.loc[glucose["code"].eq("44TK."), "recommended_use"].item()
        self.assertTrue(fasting.startswith("CONTEXT -"))
        self.assertIn("fasting", fasting)
        self.assertEqual(
            glucose.loc[glucose["code"].eq("44TK."), "code_group"].item(),
            "Fasting glucose",
        )

        all_public = "\n".join(
            path.read_text(encoding="utf-8")
            for path in Path("phenotypes").rglob("*.txt")
        )
        self.assertNotIn("422..", all_public)
        readme = Path("README.md").read_text(encoding="utf-8")
        self.assertIn("Dots are literal characters", readme)
        self.assertIn("`422..`", readme)

    def test_broad_thyroid_parent_is_not_used_as_tsh(self):
        read2 = pd.read_csv(
            "phenotypes/thyroid/gp_read2_tsh.txt",
            sep="\t",
            dtype="string",
            comment="#",
        )
        read3 = pd.read_csv(
            "phenotypes/thyroid/gp_read3_tsh.txt",
            sep="\t",
            dtype="string",
            comment="#",
        )
        self.assertNotIn("442..", set(read2["code"]))
        self.assertNotIn("442..", set(read3["code"]))
        self.assertNotIn(".442.", set(read3["code"]))
        self.assertIn("442A.", set(read2["code"]))

    def test_core_codes_have_full_lookup_audit_and_no_cross_trait_collision(self):
        catalogue = pd.read_csv(
            "catalogue/clinical_trait_codelists.csv",
            dtype="string",
            keep_default_na=False,
        )
        clinical_core = catalogue.loc[
            catalogue["trait_group"].ne("medication")
            & catalogue["selection_tier"].eq("core")
        ]
        self.assertTrue(clinical_core["all_lookup_terms"].str.len().gt(0).all())
        collisions = (
            clinical_core.groupby(["coding_system", "code"])["trait"]
            .nunique()
            .gt(1)
        )
        self.assertFalse(collisions.any())

    def test_readme_phenotype_links_exist(self) -> None:
        readme = Path("README.md").read_text(encoding="utf-8")
        links = re.findall(r"\]\((phenotypes/[^)]+)\)", readme)
        self.assertGreater(len(links), 80)
        missing = [link for link in links if not Path(link).exists()]
        self.assertEqual(missing, [])

    def test_read_v2_matching_is_exact(self) -> None:
        codes = load_codelist(
            "codelists/clinical_traits/anthropometry/body_mass_index/read_v2.csv"
        )
        observed = match_codes(pd.Series(["22K..", "22KXX", "C10.."]), codes)
        self.assertEqual(observed.tolist(), [True, False, False])

    def test_bnf_matching_uses_prefixes(self) -> None:
        codes = load_codelist(
            "codelists/medications/lipid_lowering/bnf.csv"
        )
        prefix = codes.iloc[0]["code"]
        observed = match_codes(pd.Series([prefix + "ZZZZZZ", "999999999"]), codes)
        self.assertEqual(observed.tolist(), [True, False])


if __name__ == "__main__":
    unittest.main()
