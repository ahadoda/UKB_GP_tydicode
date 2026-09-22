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
            "phenotypes/glycaemia/gp_read2_hba1c.txt", sep="\t", dtype="string"
        )
        self.assertEqual(
            hba1c.columns.tolist(), ["code", "description", "recommended_use"]
        )
        self.assertNotIn("selection_tier", hba1c.columns)
        self.assertTrue(hba1c["recommended_use"].str.len().gt(0).all())

    def test_public_guidance_distinguishes_context_and_literal_dots(self):
        glucose = pd.read_csv(
            "phenotypes/glycaemia/gp_read2_blood_glucose.txt",
            sep="\t",
            dtype="string",
        )
        fasting = glucose.loc[glucose["code"].eq("44TK."), "recommended_use"].item()
        self.assertTrue(fasting.startswith("CONTEXT -"))
        self.assertIn("fasting", fasting)

        all_public = "\n".join(
            path.read_text(encoding="utf-8")
            for path in Path("phenotypes").rglob("*.txt")
        )
        self.assertNotIn("422..", all_public)
        readme = Path("README.md").read_text(encoding="utf-8")
        self.assertIn("Dots are literal characters", readme)
        self.assertIn("`422..`", readme)

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
