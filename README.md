# FAHIMTA

**Hausa–Nigerian AI Evaluation & Improvement Framework**

FAHIMTA is a research and engineering framework for evaluating, diagnosing, and supporting improvement of Hausa/Nigerian-language AI systems.

The initial target system is **N-ATLAS**. FAHIMTA complements N-ATLAS; it does not replace or rebuild it.

## MVP research loop

**Evaluate → Diagnose → Improve → Re-evaluate**

The MVP focuses on one reproducible evaluation path rather than a broad platform.

## Current status

Research prototype scaffold — evaluation metric and verified N-ATLAS integration are still pending.

## Repository structure

```text
FAHIMTA/
├── README.md
├── docs/
│   ├── research-spec.md
│   ├── evaluation-method.md
│   └── reproducibility.md
├── src/
│   ├── evaluation/
│   ├── diagnosis/
│   └── improvement/
├── tests/
├── examples/
└── .gitignore
```

## Evidence discipline

No benchmark scores, statistical significance, superiority claims, or production-readiness claims are included without evidence.


## Latest evaluation result

**Test record:** [FAHIMTA-NATLAS-TEST-001](results/FAHIMTA-NATLAS-TEST-001.md)

- **Input:** “Menene ake nufi da gwagwarmaya?”
- **Review:** Human evaluation against the project-established Hausa standard reference.
- **Result:** **3/5 — Adequate; PASS WITH LIMITATIONS.**
- **Finding:** The captured response broadly explains effort and overcoming difficulty, but narrows *gwagwarmaya* toward confrontation and omits important rights-based, collective, and social-change meanings.
- **Evidence limitation:** The response was captured from a public N-ATLaS-branded demo. Exact backend revision/settings and direct FAHIMTA integration remain unverified.

This is one qualitative test case, not an aggregate benchmark result. The evaluator and verified N-ATLaS integration remain pending.


## Evaluation logic status (2026-10-10)

A first transparent, reviewer-scored evaluation path is now implemented in `src/evaluation/evaluator.py`. It validates reviewer-entered 1–5 ratings, computes their arithmetic mean, and records reviewer-supplied diagnostic tags. Tests for validation and scoring are in `tests/test_evaluator.py`; the method and limitations are documented in `docs/evaluation-method.md`.

**Important:** this is not an automatic semantic evaluator and does not call N-ATLaS. The existing TEST-001 overall score (3/5) remains a qualitative human judgement; no dimension-level ratings were recorded for it, so none have been fabricated. The new tests have been added to the repository, but their execution has not been independently verified in this update.


## Human evaluation rubric v1

The evaluator accepts a reviewer-assigned overall score from **0 to 5** using the project's six-level rubric: 5 Excellent, 4 Strong, 3 Adequate, 2 Weak, 1 Poor, and 0 Unusable. The rubric is recorded in the evaluation implementation and exercised by `tests/test_evaluator.py`.

The evaluator records human judgement; it does not automatically judge Hausa semantics. TEST-001 remains **3/5 — Adequate; PASS WITH LIMITATIONS**, based on the existing human review. Exact model backend provenance remains unverified, and direct N-ATLaS integration is not yet implemented.
