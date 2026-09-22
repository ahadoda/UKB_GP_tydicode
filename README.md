# UK Biobank GP cardiometabolic codelists

Use this repository to choose GP codes for common cardiometabolic research
questions. Open the relevant link below, keep the `DEFAULT` rows, and add
`CONTEXT` rows only when they match the analysis you intend to run.
Each text file contains three columns: `code`, `description`, and
`recommended_use`. The last column tells you whether the code is suitable for
a default extraction or only for a particular context, unit, or supporting use.

## How to use the files

- `gp_read2_*.txt`: match exactly and case-sensitively to `gp_clinical.read_2`.
- `gp_read3_*.txt`: match exactly and case-sensitively to `gp_clinical.read_3`.
- Use both Read 2 and Read 3 lists when extracting a clinical measurement.
- `gp_bnf_*.txt`: prefix-match to `gp_scripts.bnf_code`.
- `gp_read2drugs_*.txt`: match to `gp_scripts.read_2`.
- Keep codes as text so punctuation and leading characters are preserved.

### How to choose between similar codes

- `DEFAULT`: include for the usual version of that phenotype.
- `CONTEXT`: include only when its stated specimen, posture, timing, fraction,
  or calculation method matches the research question.
- `UNIT-SPECIFIC`: include only with the stated unit convention, or harmonise
  values before pooling.
- `SUPPORTING`: useful for finding related records, but not interchangeable
  with the main numeric phenotype.

Dots are literal characters in Read codes, not wildcards. For example,
`422..` is the complete code for `O/E: inspection of blood`; it does **not**
mean every code beginning with `422`. It describes visual inspection of blood,
not a numeric blood biomarker, so it is deliberately excluded from these
measurement codelists.

## Body size and adiposity

| Research measure | Read 2 codes | Read 3 codes |
|---|---|---|
| Body weight | [open list](phenotypes/anthropometry/gp_read2_body_weight.txt) | [open list](phenotypes/anthropometry/gp_read3_body_weight.txt) |
| Body height | [open list](phenotypes/anthropometry/gp_read2_body_height.txt) | [open list](phenotypes/anthropometry/gp_read3_body_height.txt) |
| BMI | [open list](phenotypes/anthropometry/gp_read2_body_mass_index.txt) | [open list](phenotypes/anthropometry/gp_read3_body_mass_index.txt) |
| Waist circumference | [open list](phenotypes/anthropometry/gp_read2_waist_circumference.txt) | [open list](phenotypes/anthropometry/gp_read3_waist_circumference.txt) |
| Hip circumference | [open list](phenotypes/anthropometry/gp_read2_hip_circumference.txt) | [open list](phenotypes/anthropometry/gp_read3_hip_circumference.txt) |

## Blood pressure

| Research measure | Read 2 codes | Read 3 codes |
|---|---|---|
| Systolic blood pressure | [open list](phenotypes/haemodynamics/gp_read2_systolic_blood_pressure.txt) | [open list](phenotypes/haemodynamics/gp_read3_systolic_blood_pressure.txt) |
| Diastolic blood pressure | [open list](phenotypes/haemodynamics/gp_read2_diastolic_blood_pressure.txt) | [open list](phenotypes/haemodynamics/gp_read3_diastolic_blood_pressure.txt) |
| Generic blood-pressure records | [open list](phenotypes/haemodynamics/gp_read2_blood_pressure.txt) | [open list](phenotypes/haemodynamics/gp_read3_blood_pressure.txt) |

For numeric analyses, use the systolic and diastolic lists. Use the generic list
only when combined or non-component blood-pressure records are relevant.

## Glycaemia and diabetes monitoring

| Research question | Read 2 codes | Read 3 codes |
|---|---|---|
| Long-term glycaemic control: HbA1c | [open list](phenotypes/glycaemia/gp_read2_hba1c.txt) | [open list](phenotypes/glycaemia/gp_read3_hba1c.txt) |
| Current glycaemia: blood glucose | [open list](phenotypes/glycaemia/gp_read2_blood_glucose.txt) | [open list](phenotypes/glycaemia/gp_read3_blood_glucose.txt) |
| Circulating insulin | [open list](phenotypes/glycaemia/gp_read2_insulin.txt) | [open list](phenotypes/glycaemia/gp_read3_insulin.txt) |
| Endogenous insulin secretion: C-peptide | [open list](phenotypes/glycaemia/gp_read2_c_peptide.txt) | [open list](phenotypes/glycaemia/gp_read3_c_peptide.txt) |

## Lipids and cardiovascular risk

| Research measure | Read 2 codes | Read 3 codes |
|---|---|---|
| Total cholesterol | [open list](phenotypes/lipids/gp_read2_total_cholesterol.txt) | [open list](phenotypes/lipids/gp_read3_total_cholesterol.txt) |
| HDL cholesterol | [open list](phenotypes/lipids/gp_read2_hdl_cholesterol.txt) | [open list](phenotypes/lipids/gp_read3_hdl_cholesterol.txt) |
| LDL cholesterol | [open list](phenotypes/lipids/gp_read2_ldl_cholesterol.txt) | [open list](phenotypes/lipids/gp_read3_ldl_cholesterol.txt) |
| Triglycerides | [open list](phenotypes/lipids/gp_read2_triglycerides.txt) | [open list](phenotypes/lipids/gp_read3_triglycerides.txt) |
| Apolipoprotein A-I | [open list](phenotypes/lipids/gp_read2_apolipoprotein_a.txt) | [open list](phenotypes/lipids/gp_read3_apolipoprotein_a.txt) |
| Apolipoprotein B | [open list](phenotypes/lipids/gp_read2_apolipoprotein_b.txt) | [open list](phenotypes/lipids/gp_read3_apolipoprotein_b.txt) |
| Lipoprotein(a) | [open list](phenotypes/lipids/gp_read2_lipoprotein_a.txt) | [open list](phenotypes/lipids/gp_read3_lipoprotein_a.txt) |

## Kidney function and kidney damage

| Research measure | Read 2 codes | Read 3 codes |
|---|---|---|
| Creatinine | [open list](phenotypes/renal/gp_read2_creatinine.txt) | [open list](phenotypes/renal/gp_read3_creatinine.txt) |
| eGFR | [open list](phenotypes/renal/gp_read2_egfr.txt) | [open list](phenotypes/renal/gp_read3_egfr.txt) |
| Urine albumin-creatinine ratio | [open list](phenotypes/renal/gp_read2_albumin_creatinine_ratio.txt) | [open list](phenotypes/renal/gp_read3_albumin_creatinine_ratio.txt) |
| Cystatin C | [open list](phenotypes/renal/gp_read2_cystatin_c.txt) | [open list](phenotypes/renal/gp_read3_cystatin_c.txt) |
| Urea | [open list](phenotypes/renal/gp_read2_urea.txt) | [open list](phenotypes/renal/gp_read3_urea.txt) |

## Liver, inflammation and other metabolic biomarkers

| Research measure | Read 2 codes | Read 3 codes |
|---|---|---|
| ALT | [open list](phenotypes/liver/gp_read2_alanine_aminotransferase.txt) | [open list](phenotypes/liver/gp_read3_alanine_aminotransferase.txt) |
| AST | [open list](phenotypes/liver/gp_read2_aspartate_aminotransferase.txt) | [open list](phenotypes/liver/gp_read3_aspartate_aminotransferase.txt) |
| GGT | [open list](phenotypes/liver/gp_read2_gamma_glutamyl_transferase.txt) | [open list](phenotypes/liver/gp_read3_gamma_glutamyl_transferase.txt) |
| Alkaline phosphatase | [open list](phenotypes/liver/gp_read2_alkaline_phosphatase.txt) | [open list](phenotypes/liver/gp_read3_alkaline_phosphatase.txt) |
| Serum albumin | [open list](phenotypes/liver/gp_read2_albumin.txt) | [open list](phenotypes/liver/gp_read3_albumin.txt) |
| Bilirubin | [open list](phenotypes/liver/gp_read2_bilirubin.txt) | [open list](phenotypes/liver/gp_read3_bilirubin.txt) |
| C-reactive protein | [Read 2](phenotypes/inflammation/gp_read2_c_reactive_protein.txt) | [Read 3](phenotypes/inflammation/gp_read3_c_reactive_protein.txt) |
| Urate | [Read 2](phenotypes/metabolic/gp_read2_urate.txt) | [Read 3](phenotypes/metabolic/gp_read3_urate.txt) |
| Calcium | [Read 2](phenotypes/metabolic/gp_read2_calcium.txt) | [Read 3](phenotypes/metabolic/gp_read3_calcium.txt) |
| Phosphate | [Read 2](phenotypes/metabolic/gp_read2_phosphate.txt) | [Read 3](phenotypes/metabolic/gp_read3_phosphate.txt) |
| 25-hydroxyvitamin D | [Read 2](phenotypes/metabolic/gp_read2_vitamin_d.txt) | [Read 3](phenotypes/metabolic/gp_read3_vitamin_d.txt) |

## Thyroid function

| Research question | Read 2 codes | Read 3 codes |
|---|---|---|
| Initial thyroid assessment: TSH | [open list](phenotypes/thyroid/gp_read2_tsh.txt) | [open list](phenotypes/thyroid/gp_read3_tsh.txt) |
| Thyroid hormone status: free T4 | [open list](phenotypes/thyroid/gp_read2_free_t4.txt) | [open list](phenotypes/thyroid/gp_read3_free_t4.txt) |
| Thyrotoxicosis assessment: free T3 | [open list](phenotypes/thyroid/gp_read2_free_t3.txt) | [open list](phenotypes/thyroid/gp_read3_free_t3.txt) |
| Autoimmune thyroid disease: TPO antibody | [open list](phenotypes/thyroid/gp_read2_thyroid_peroxidase_antibody.txt) | [open list](phenotypes/thyroid/gp_read3_thyroid_peroxidase_antibody.txt) |
| Thyroglobulin antibody | not available in supplied Read 2 lookup | [open list](phenotypes/thyroid/gp_read3_thyroglobulin_antibody.txt) |

## Blood count and biological age

| Research measure | Read 2 codes | Read 3 codes |
|---|---|---|
| White blood cell count | [open list](phenotypes/haematology/gp_read2_white_blood_cell_count.txt) | [open list](phenotypes/haematology/gp_read3_white_blood_cell_count.txt) |
| Mean corpuscular volume | [open list](phenotypes/haematology/gp_read2_mean_corpuscular_volume.txt) | [open list](phenotypes/haematology/gp_read3_mean_corpuscular_volume.txt) |
| Red cell distribution width | [open list](phenotypes/haematology/gp_read2_red_cell_distribution_width.txt) | [open list](phenotypes/haematology/gp_read3_red_cell_distribution_width.txt) |
| Haemoglobin | [open list](phenotypes/haematology/gp_read2_haemoglobin.txt) | [open list](phenotypes/haematology/gp_read3_haemoglobin.txt) |
| Platelet count | [open list](phenotypes/haematology/gp_read2_platelet_count.txt) | [open list](phenotypes/haematology/gp_read3_platelet_count.txt) |

For the published PhenoAge algorithm, use albumin, alkaline phosphatase,
creatinine, glucose, CRP, white blood cell count, MCV and RDW from the lists
above, plus chronological age and lymphocyte percentage. UK Biobank provides
lymphocyte percentage directly in its baseline blood-count data; it is not
represented as a GP codelist here.

## Cardiometabolic prescriptions

| Exposure | BNF prefixes | Read 2 drug codes |
|---|---|---|
| Glucose-lowering medicines | [open list](phenotypes/medications/gp_bnf_glucose_lowering.txt) | [open list](phenotypes/medications/gp_read2drugs_glucose_lowering.txt) |
| Antihypertensive medicines | [open list](phenotypes/medications/gp_bnf_antihypertensive.txt) | [open list](phenotypes/medications/gp_read2drugs_antihypertensive.txt) |
| Lipid-lowering medicines | [open list](phenotypes/medications/gp_bnf_lipid_lowering.txt) | [open list](phenotypes/medications/gp_read2drugs_lipid_lowering.txt) |
| Weight-management medicines | [open list](phenotypes/medications/gp_bnf_weight_management.txt) | [open list](phenotypes/medications/gp_read2drugs_weight_management.txt) |

## Numeric results

After matching a clinical code, inspect `value1`, `value2` and `value3` to find
the recorded result. Confirm units before combining records, and retain the
original value and unit. The expected unit for every list is available in the
[complete index](phenotypes/index.csv).

The `catalogue`, `src`, `tests` and detailed `docs` folders support maintenance
and reproducibility. They are not required for choosing a codelist.

## Licence and attribution

This repository is available under the
[Open Government Licence v3.0](LICENSE). It contains Read terminology
information from NHS Digital and BNF Code Information from NHSBSA. Required
source acknowledgements are provided in [NOTICE.md](NOTICE.md). The repository
contains no UK Biobank participant-level data.
