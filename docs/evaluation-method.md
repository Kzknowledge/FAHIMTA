# Evaluation Method

## MVP method: reviewer-scored rubric

FAHIMTA accepts a recorded input, reference/expected behaviour, target-system output, and explicit human reviewer ratings. The evaluator validates the record and calculates the arithmetic mean of the supplied ratings. It does **not** automatically infer semantic correctness from text.

Implementation: `src/evaluation/evaluator.py`.

## Rubric dimensions

Ratings use an integer scale from 1 to 5 for any explicitly assessed dimensions:

1. `core_meaning` — whether the core meaning is represented.
2. `goal_orientation` — whether goals such as progress, rights, justice, or change are represented where relevant.
3. `individual_and_collective_scope` — whether personal and collective meanings are appropriately covered.
4. `non_force_methods` — whether non-force means are recognized where relevant.
5. `contextual_valence` — whether the response preserves context-dependent positive/negative meaning.

Reviewers must provide a short rationale and supporting evidence in the case record. Ratings must not be backfilled or invented to fit a previously assigned overall judgement. The five dimensions are a proposed operational rubric and should be validated by Hausa-language reviewers before formal benchmark use.

## Score interpretation and limitations

The implementation computes the unrounded arithmetic mean of the reviewer-entered dimension ratings. This number is descriptive only: it is not a probability, automated semantic score, accuracy estimate, or statistically validated benchmark result. Because a subset of dimensions can be supplied, reports must list which dimensions were actually rated.

The existing TEST-001 judgement of 3/5 was a qualitative overall human assessment. No dimension-level ratings were recorded for that assessment, so the implementation must not manufacture dimension ratings or claim that the code independently reproduced that score.

## Diagnostic tags

Reviewer-supplied tags may include `semantic-narrowing`, `confrontation-overemphasis`, `omitted-collective-scope`, `omitted-rights-and-social-change`, and `non-force-methods-underrepresented`. Tags trigger a review recommendation; they do not prove a root cause.

## Procedure

1. Preserve the exact input and target-system output.
2. Preserve the reference answer and evaluation method version.
3. Have a reviewer rate relevant rubric dimensions from 1 to 5 and explain each rating.
4. Record diagnostic tags only when supported by the response.
5. Compute and record the mean of the ratings actually supplied.
6. Review suggested follow-up actions; a recommendation is not an intervention.
7. Re-evaluate after a documented intervention using the same procedure where possible.

## N-ATLaS integration

The evaluator is system-agnostic. A replaceable adapter boundary is defined, but this implementation does not call N-ATLaS. A verified model endpoint, model revision, and execution configuration are still required for direct integration.

## Evidence discipline

No benchmark score is predefined. Do not claim statistical significance, overall model accuracy, superiority, or improvement without appropriate evidence and a documented evaluation design.
