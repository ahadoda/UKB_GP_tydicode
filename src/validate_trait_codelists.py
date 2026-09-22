from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {
    "trait_id", "trait_group", "trait", "coding_system", "source_dataset",
    "source_field", "match_type", "case_sensitive", "code", "description",
    "all_lookup_terms", "selection_tier", "value_type", "expected_units", "source_sheet",
    "review_status",
}


def main() -> int:
    manifest_path = ROOT / "catalogue" / "trait_manifest.csv"
    master_path = ROOT / "catalogue" / "clinical_trait_codelists.csv"
    scope_path = ROOT / "catalogue" / "biomarker_scope.csv"
    public_index_path = ROOT / "phenotypes" / "index.csv"
    errors: list[str] = []
    if (
        not manifest_path.exists()
        or not master_path.exists()
        or not scope_path.exists()
        or not public_index_path.exists()
    ):
        print("Generated files are missing. Run src/build_trait_codelists.py.")
        return 1
    manifest = pd.read_csv(manifest_path, dtype="string", keep_default_na=False)
    master = pd.read_csv(master_path, dtype="string", keep_default_na=False)
    scope = pd.read_csv(scope_path, dtype="string", keep_default_na=False)
    public_index = pd.read_csv(public_index_path, dtype="string", keep_default_na=False)
    scope_required = {
        "domain", "biomarker", "priority", "recommended_source", "role",
        "biological_age_role", "notes",
    }
    if missing_scope := scope_required.difference(scope.columns):
        errors.append(f"biomarker_scope.csv: missing {sorted(missing_scope)}")
    if not set(scope["priority"]).issubset({"core", "secondary", "context-specific"}):
        errors.append("biomarker_scope.csv: invalid priority")
    public_required = {
        "research_use", "phenotype", "ukb_table", "ukb_field", "coding_system",
        "matching", "expected_units", "code_count", "codelist",
    }
    if missing_public := public_required.difference(public_index.columns):
        errors.append(f"phenotypes/index.csv: missing {sorted(missing_public)}")
    for record in public_index.to_dict("records"):
        path = ROOT / record["codelist"]
        if not path.exists():
            errors.append(f"Missing public codelist: {record['codelist']}")
            continue
        data = pd.read_csv(
            path, sep="\t", dtype="string", keep_default_na=False, comment="#"
        )
        if list(data.columns) != [
            "code", "description", "code_group", "recommended_use"
        ]:
            errors.append(
                f"{record['codelist']}: expected code, description, code_group and recommended_use"
            )
        elif data["code_group"].eq("").any() or data["recommended_use"].eq("").any():
            errors.append(f"{record['codelist']}: blank code_group or recommended_use")
        if len(data) != int(record["code_count"]):
            errors.append(f"{record['codelist']}: public index count mismatch")
    total = 0
    for record in manifest.to_dict("records"):
        path = ROOT / record["path"]
        if not path.exists():
            errors.append(f"Missing file: {record['path']}")
            continue
        data = pd.read_csv(path, dtype="string", keep_default_na=False)
        missing = REQUIRED.difference(data.columns)
        if missing:
            errors.append(f"{record['path']}: missing {sorted(missing)}")
            continue
        if data["code"].str.strip().eq("").any():
            errors.append(f"{record['path']}: blank code")
        if data["code"].duplicated().any():
            errors.append(f"{record['path']}: duplicate code")
        if not set(data["selection_tier"]).issubset({"core", "extended_review"}):
            errors.append(f"{record['path']}: invalid selection tier")
        if len(data) != int(record["total_rows"]):
            errors.append(f"{record['path']}: manifest count mismatch")
        total += len(data)
    if len(master) != total:
        errors.append(f"Master row count {len(master)} does not equal {total}")
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Validation passed: {len(manifest)} codelists and {len(master)} rows.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
