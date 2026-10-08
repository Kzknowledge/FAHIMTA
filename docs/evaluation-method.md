# Evaluation Method

## MVP method

Each evaluation case is represented as a structured record containing an input, expected behavior where applicable, N-ATLAS output, evaluation method, score, diagnosis, improvement action, and re-evaluation result.

The evaluator boundary is intentionally system-agnostic. N-ATLAS integration will be added through a replaceable adapter/interface once its actual interface is verified.

## Required method definition

Every implemented metric must document:

1. Definition
2. Scoring rule
3. Rationale
4. Evaluation procedure
5. Limitation

## Scoring

No benchmark score is predefined by this scaffold. Scores must be produced only by an implemented and documented evaluation procedure applied to actual evaluation cases.

## Re-evaluation

An improvement recommendation is not evidence of improvement by itself. Where an intervention is applied, the affected case must be evaluated again using the same or explicitly revised procedure.
