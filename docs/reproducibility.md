# Reproducibility

A reproducible FAHIMTA evaluation should preserve enough information for another researcher to understand and repeat the evaluation.

## Minimum evaluation record

- evaluation_id
- input
- expected_behavior
- n_atlas_output
- evaluation_method
- score
- error_category
- diagnosis
- improvement_action
- re_evaluation_result
- timestamp
- version

## Environment

The MVP should record the software version, execution environment, and any external model/system version needed to reproduce the case.

## Reproducibility rule

Do not claim an evaluation is reproducible unless the input, method, scoring rule, relevant system output, and execution/version context are preserved.