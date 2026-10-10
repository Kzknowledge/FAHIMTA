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
