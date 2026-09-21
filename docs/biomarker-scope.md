# Biomarker scope for cardiometabolic research

The recommended panel is deliberately tiered. `Core` markers should cover most
cardiometabolic analyses. `Secondary` markers add mechanistic or biological-age
information. `Context-specific` markers should be included only when the study
question justifies them. The machine-readable version is
[`catalogue/biomarker_scope.csv`](../catalogue/biomarker_scope.csv).

## Recommended core panel

| Domain | Core variables |
|---|---|
| Adiposity | weight, BMI, waist circumference |
| Blood pressure | systolic and diastolic blood pressure |
| Glycaemia | HbA1c and glucose |
| Lipids | total, HDL and LDL cholesterol; triglycerides; ApoB; lipoprotein(a) |
| Kidney | creatinine, eGFR and urine albumin-creatinine ratio |
| Liver/inflammation | ALT, GGT, albumin, alkaline phosphatase and CRP |
| Thyroid | TSH and free T4 |
| Blood count | white-cell count, lymphocyte percentage, MCV, RDW and haemoglobin |
| Other metabolic | urate |

Insulin and C-peptide are useful but are not default core markers because they
are less consistently available and answer more specialised questions.

## Thyroid testing

For adults without suspected pituitary disease, use TSH as the initial test.
Add free T4 when TSH is above the reference range, and add free T4 plus free T3
when TSH is below it. TSH and free T4 together are appropriate when secondary
thyroid dysfunction is suspected. Thyroid peroxidase and thyroglobulin
antibodies are context-specific aetiological markers, not routine repeated
outcomes. These choices follow the testing cascade in the
[NICE thyroid guideline](https://www.nice.org.uk/guidance/ng145/chapter/Recommendations).

## Biological age

The published PhenoAge blood-chemistry algorithm uses chronological age plus:

- albumin;
- alkaline phosphatase;
- creatinine;
- glucose;
- C-reactive protein;
- lymphocyte percentage;
- mean corpuscular volume;
- red cell distribution width; and
- white blood cell count.

Do not label an incomplete subset as PhenoAge, and do not substitute HbA1c for
glucose without validating a different algorithm. Apply the published formula,
transformations and units. The marker set is documented in the
[BioAge methods paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC8602613/) and has
also been evaluated in UK Biobank analyses of biological-age phenotypes.

## Choose the right source

UK Biobank directly measured a broad serum biochemistry panel and full blood
count at baseline, with repeat biomarker measurements in a subset. For a
cross-sectional baseline analysis, those structured fields are normally
preferable to reconstructing the same values from GP records. See the official
[UK Biobank biomarker overview](https://www.ukbiobank.ac.uk/about-our-data/types-of-data/biomarker-data/),
[serum biochemistry companion document](https://biobank.ndph.ox.ac.uk/showcase/ukb/docs/serum_biochemistry.pdf),
and [haematology companion document](https://biobank.ndph.ox.ac.uk/ukb/ukb/docs/haematology.pdf).

GP codelists remain valuable for longitudinal measurements before and after
baseline, thyroid tests not included in the standard serum panel, and clinical
monitoring between assessment visits. Keep UKB assessment and GP observations
as separate source layers until units, specimen type, timing and assay context
have been harmonised.

## Extensions

Common secondary extensions are cystatin C, urea, AST, bilirubin, calcium,
phosphate, vitamin D and platelet count. IGF-1, testosterone/SHBG, thyroid
antibodies, insulin and C-peptide are context-specific rather than universal.
This prevents the catalogue from becoming an indiscriminate list of every
available assay.
