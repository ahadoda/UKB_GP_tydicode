# Data dictionary

| Field | Meaning |
| --- | --- |
| `trait_id` | Stable identifier combining trait, group, and coding system. |
| `trait_group` | Clinical trait family or medication. |
| `trait` | Specific clinical measurement or prescription group. |
| `coding_system` | Read v2, CTV3, BNF, or Read v2 drug code. |
| `source_dataset` | UK Biobank GP table to search. |
| `source_field` | Field to match, such as `read_2`, `read_3`, or `bnf_code`. |
| `match_type` | Exact code matching or prefix matching. |
| `case_sensitive` | Whether letter case must be preserved. |
| `code` | Terminology code or BNF prefix. Always treat as text. |
| `description` | Representative source description. |
| `matched_terms` | Source descriptions that triggered selection. |
| `selection_tier` | `core` or `extended_review`. |
| `value_type` | Numeric-measurement candidate or prescription exposure. |
| `expected_units` | Unit guidance for review, not a stored-value guarantee. |
| `source_sheet` | Worksheet in `all_lkps_maps_v4.xlsx`. |
| `source_metadata` | Term information or BNF hierarchy context. |
| `review_status` | Required domain-review status. |

The builder consolidates terminology synonyms to one entry per trait and code
while retaining matched descriptions in `matched_terms`.

