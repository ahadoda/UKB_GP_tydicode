from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


def load_manifest() -> pd.DataFrame:
    return pd.read_csv(
        ROOT / "catalogue" / "trait_manifest.csv",
        dtype="string",
        keep_default_na=False,
    )


def load_codelist(path: str | Path, tier: str = "core") -> pd.DataFrame:
    """Load one codelist. By default only clinically reviewable core candidates are returned."""
    source = Path(path)
    if not source.is_absolute():
        source = ROOT / source
    data = pd.read_csv(source, dtype="string", keep_default_na=False)
    if tier == "all":
        return data
    if tier not in {"core", "extended_review"}:
        raise ValueError("tier must be 'core', 'extended_review', or 'all'")
    return data[data["selection_tier"].eq(tier)].copy()


def match_codes(values: pd.Series, codelist: pd.DataFrame) -> pd.Series:
    rules = codelist[["match_type", "case_sensitive"]].drop_duplicates()
    if len(rules) != 1:
        raise ValueError("Expected one matching rule per codelist")
    rule = rules.iloc[0]
    observed = values.astype("string").fillna("")
    codes = codelist["code"].astype("string").tolist()
    if rule["case_sensitive"].casefold() != "true":
        observed = observed.str.casefold()
        codes = [code.casefold() for code in codes]
    if rule["match_type"] == "exact":
        return observed.isin(codes)
    if rule["match_type"] == "prefix":
        return observed.str.startswith(tuple(codes), na=False)
    raise ValueError(f"Unsupported match type: {rule['match_type']}")

