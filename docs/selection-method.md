# Selection method

## Clinical traits

The builder searches descriptions in `read_v2_lkp` and `read_ctv3_lkp` using
trait-specific inclusion and exclusion expressions. It consolidates synonyms
to one row per trait and code.

`core` candidates contain terminology that looks like a direct measurement or
result and avoids qualitative labels such as high, low, normal, target, or
declined. `extended_review` contains related terms that may still be useful but
need closer inspection.

Terminology text alone cannot prove that a GP record contains a usable numeric
value. Review matched records in the actual UK Biobank release before freezing
an analysis codelist.

## Medication groups

Medication candidates use named BNF hierarchy categories:

- Glucose lowering: Antidiabetic Drugs and Insulin within Drugs Used In Diabetes.
- Lipid lowering: Lipid-Regulating Drugs.
- Weight management: Obesity.
- Antihypertensive: ACE inhibitors, angiotensin-II receptor antagonists,
  beta blockers, calcium-channel blockers, centrally acting drugs,
  vasodilator antihypertensives, and thiazide-related diuretics.

BNF output uses the first nine characters, corresponding to the chemical
substance level described by the source workbook. Read v2 drug candidates are
derived through `read_v2_drugs_bnf`.

The antihypertensive classes are not exhaustive for every definition. Loop
diuretics and mineralocorticoid antagonists are not included by default because
their indication is often not hypertension.

## Review workflow

1. Review core descriptions with a clinician and clinical coder.
2. Inspect actual matched records and value-field completeness.
3. Decide whether extended candidates improve coverage without harming specificity.
4. Review medication classes with a pharmacist or pharmacoepidemiologist.
5. Freeze reviewed lists in a study-specific version and document changes.

