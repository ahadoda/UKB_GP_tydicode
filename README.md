# UK Biobank GP clinical trait codelists

This repository provides an original, trait-centred catalogue for UK Biobank
primary-care data. It is generated from the local UK Biobank lookup workbook,
`all_lkps_maps_v4.xlsx`, rather than copied from a disease-phenotype
repository.

The main focus is repeated clinical traits:

- Anthropometry: weight, height, BMI, waist, and hip. Waist-to-hip ratio can be
  derived after compatible waist and hip measurements are selected.
- Haemodynamics: systolic, diastolic, and generic blood-pressure records.
- Glycaemia: glucose, HbA1c, insulin, and C-peptide.
- Lipids: total, HDL and LDL cholesterol, triglycerides, apolipoproteins, and
  lipoprotein(a).
- Renal markers: creatinine, eGFR, urine albumin-creatinine ratio, urea, and
  cystatin C.
- Liver and inflammatory markers: ALT, AST, GGT, alkaline phosphatase,
  albumin, bilirubin, CRP, and urate.
- Thyroid function: TSH, free T4, free T3, and context-specific antibodies.
- Blood count and biological-age inputs: white-cell count, MCV, RDW,
  haemoglobin, and platelets. Lymphocyte percentage is identified as a required
  UKB blood-count field rather than forced into a GP codelist.
- Optional prescription groups: glucose-lowering, lipid-lowering,
  antihypertensive, and weight-management medicines.

## Important status

The generated lists are candidates selected from terminology descriptions and
BNF hierarchy fields. They are not validated phenotypes. Every list carries a
`review_status`, and extended candidates are separated from the narrower
`core` tier.

## Start here

1. Review [the selection method](docs/selection-method.md).
2. Use [the biomarker scope](docs/biomarker-scope.md) to choose a core,
   secondary, or context-specific panel and the preferred data source.
3. Choose a list from [the trait manifest](catalogue/trait_manifest.csv).
4. Start with `selection_tier == "core"`.
5. Clinically review the descriptions and expected value fields.
6. Follow [the usage guide](docs/usage-guide.md) for matching and value checks.

## Structure

```text
catalogue/
  trait_manifest.csv
  clinical_trait_codelists.csv
  review_summary.csv
  selection_rules.csv
  biomarker_scope.csv
codelists/
  clinical_traits/
  medications/
docs/
src/
```

## Build and validation

```text
python src/build_trait_codelists.py
python src/validate_trait_codelists.py
```

The build is reproducible from the lookup workbook in the parent
`primarycare_codings` directory. It does not modify that workbook.
