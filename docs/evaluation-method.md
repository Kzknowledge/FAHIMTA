# Evaluation Method

## MVP method: reviewer-assigned overall score

FAHIMTA records a target-system input, expected/reference behaviour, captured output, and one explicit human-assigned overall score from 0 to 5. The evaluator validates and records that judgement; it does not automatically infer semantic correctness from text and does not calculate a mean across dimension ratings.

Implementation: `src/evaluation/evaluator.py`.

## Overall score rubric

The current implementation uses the following six-level rubric:

- **5 — Excellent:** Gives the broad definition, includes goal-oriented effort and overcoming difficulty, recognizes individual/collective and peaceful/nonviolent forms, and notes contextual valence.
- **4 — Strong:** Correctly explains sustained effort toward a goal or overcoming hardship; includes at least one non-force dimension such as rights, progress, or change.
- **3 — Adequate:** Captures effort/struggle against difficulty but is somewhat narrow, repetitive, or misses collective/social change.
- **2 — Weak:** Gives only a partial or overly physical meaning, such as fighting or defeating someone, without the broader sense of striving or resistance.
- **1 — Poor:** Wrong meaning, major factual/linguistic error, or irrelevant response.
- **0 — Unusable:** No meaningful answer, refusal without reason, or response in the wrong language.

The score is a reviewer judgement. It is not a probability, automated semantic score, accuracy estimate, or statistically validated benchmark result.

## Proposed future dimensions (not implemented as score inputs)

The following dimensions may support more granular future reviews:

1. `core_meaning` — whether the core meaning is represented.
2. `goal_orientation` — whether goals such as progress, rights, justice, or change are represented where relevant.
3. `individual_and_collective_scope` — whether personal and collective meanings are appropriately covered.
4. `non_force_methods` — whether non-force means are recognized where relevant.
5. `contextual_valence` — whether the response preserves context-dependent positive/negative meaning.

These dimensions are proposed and should be reviewed by Hausa-language reviewers before formal benchmark use. The current evaluator does not accept dimension-level ratings or compute their arithmetic mean. Do not report such scores unless the implementation and case records are explicitly extended to support them.

The existing TEST-001 judgement of 3/5 was a qualitative overall human assessment. No dimension-level ratings were recorded for that assessment, so none should be manufactured or claimed to have been reproduced by code.

## Diagnostic tags

Reviewer-supplied tags may include `semantic-narrowing`, `confrontation-overemphasis`, `omitted-collective-scope`, `omitted-rights-and-social-change`, and `non-force-methods-underrepresented`. Tags trigger a review recommendation; they do not prove a root cause.

## Procedure

1. Preserve the exact input and target-system output.
2. Preserve the reference answer and evaluation method version.
3. Assign one overall score from 0 to 5 using the rubric above.
4. Record a short reviewer rationale and diagnostic tags only when supported by the response.
5. Review suggested follow-up actions; a recommendation is not an intervention.
6. Re-evaluate after a documented intervention using the same procedure where possible.

## N-ATLaS integration

The evaluator is system-agnostic. A replaceable adapter boundary is defined, but this implementation does not call N-ATLaS. A verified model endpoint, model revision, and execution configuration are still required for direct integration.

## Evidence discipline

No benchmark score is predefined. Do not claim statistical significance, overall model accuracy, superiority, or improvement without appropriate evidence and a documented evaluation design.
