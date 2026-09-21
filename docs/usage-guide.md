# Usage guide

## 1. Choose the clinical trait

First use `catalogue/biomarker_scope.csv` to decide whether the preferred
source is a UKB assessment field, a GP record, or a derived value. Then use
`catalogue/trait_manifest.csv` for GP extraction. Select the coding system corresponding to
the available field:

- `read_v2` with `gp_clinical.read_2`
- `ctv3` with `gp_clinical.read_3`
- `bnf` with `gp_scripts.bnf_code`
- `read_v2_drug` with `gp_scripts.read_2`

Use both primary-care clinical coding fields when coverage across systems is
required. Do not apply Read v2 codes to the Read 3 field or vice versa.

## 2. Review before use

Begin with the `core` tier. Review every code description against the intended
trait, population, time period, and data release. Add `extended_review` only
after inspecting its broader or qualitative concepts.

The catalogue identifies candidate records. It does not decide which numeric
field contains the result, validate units, remove impossible values, aggregate
same-day records, or define baseline and follow-up windows.

## 3. Match codes

```python
import pandas as pd

from src.trait_codelists import load_codelist, match_codes

bmi_codes = load_codelist(
    "codelists/clinical_traits/anthropometry/body_mass_index/read_v2.csv",
    tier="core",
)
clinical = pd.read_csv("gp_clinical.csv", dtype="string")
clinical["is_bmi_record"] = match_codes(clinical["read_2"], bmi_codes)
```

Clinical trait codes use exact, case-sensitive matching. BNF medication lists
use prefix matching. Keep codes as strings and preserve punctuation.

In R, exact matching can use `%in%`:

```r
library(readr)

codes <- read_csv(
  "codelists/clinical_traits/glycaemia/hba1c/read_v2.csv",
  col_types = cols(.default = col_character())
)
codes <- subset(codes, selection_tier == "core")
clinical$is_hba1c_record <- clinical$read_2 %in% codes$code
```

For a BNF prefix list, use `startsWith()` for each observed code and report the
combination rule used when several medication fields are searched.

## 4. Locate and validate the value

UK Biobank GP records can store results in `value1`, `value2`, or `value3`, and
some records use an operator or sentinel in one value field. For each trait:

1. Inspect matched records across all value fields.
2. Confirm the code-specific unit and the unit field where available.
3. Convert units explicitly and retain the original value and unit.
4. Define plausible-range rules in the study protocol.
5. Resolve multiple measurements on the same date consistently.
6. Keep a record-level exclusion reason for rejected observations.

The `expected_units` field is review guidance. It must not be used to overwrite
or assume a missing unit.

## 5. Prescription groups

Prescription lists are optional covariates or exposure definitions. BNF lists
are built from BNF hierarchy categories. Read v2 drug lists are derived through
the workbook's Read v2-to-BNF mapping. Because `gp_scripts` fields are not
uniformly populated, consider both fields and document the combination rule.

Medication presence does not establish a diagnosis. Indication, dose,
duration, adherence, and combination products require separate review.

## 6. Report the implementation

Record the repository commit, `trait_id`, selection tier, coding systems,
matched source fields, unit conversion, plausible ranges, date handling,
duplicate handling, and any code additions or exclusions.
