# FAHIMTA

**Hausa–Nigerian AI Evaluation & Improvement Framework**

FAHIMTA is a research and engineering framework for evaluating, diagnosing, and supporting improvement of Hausa/Nigerian-language AI systems.

The initial target system is **N-ATLAS**. FAHIMTA complements N-ATLAS; it does not replace or rebuild it.

## MVP research loop

**Evaluate → Diagnose → Improve → Re-evaluate**

The MVP focuses on a narrow, documented evaluation path rather than a broad platform.

## Current status

Research prototype scaffold with a reviewer-assigned overall-score evaluator and smoke tests. The full repository has not yet been verified from a fresh clone, and direct N-ATLaS integration is not implemented.

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

This is one qualitative human-reviewed case, not an aggregate benchmark result.

## Evaluator status (2026-10-10)

The evaluator in `src/evaluation/evaluator.py` validates and records a reviewer-assigned overall score from **0 to 5**, along with reviewer-supplied diagnostic tags and rationale. It does not automatically evaluate Hausa semantics, accept dimension-level ratings, calculate a mean across dimensions, or call N-ATLaS.

The rubric is documented in `docs/evaluation-method.md` and exercised by `tests/test_evaluator.py`. A local test run of the reconstructed evaluator and smoke-test files reported **16 passed**. This is a limited local verification of the retrieved files, not yet a full test of a fresh clone of the entire repository. GitHub Actions did not start because of an account restriction; that status does not indicate a code-test failure or success.

TEST-001 remains **3/5 — Adequate; PASS WITH LIMITATIONS**, based on human review. No dimension-level ratings have been invented. Exact model backend provenance remains unverified, and direct N-ATLaS integration is not yet implemented.
