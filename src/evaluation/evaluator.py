"""Transparent human-scored evaluation for recorded model outputs.

The overall score is assigned by a reviewer using FAHIMTA's documented 0–5
rubric. This module validates and records that judgement; it does not infer
semantic quality automatically.
"""
from typing import Mapping, Optional, Protocol, Sequence

from .models import EvaluationRecord


class NAtlasAdapter(Protocol):
    """Minimal adapter boundary for an actual N-ATLaS integration."""

    def evaluate(self, input_text: str) -> str:
        """Return the target system's response for an input."""
        ...


SCORE_LABELS = {
    0: "Unusable",
    1: "Poor",
    2: "Weak",
    3: "Adequate",
    4: "Strong",
    5: "Excellent",
}

SCORE_DESCRIPTIONS = {
    5: (
        "Gives the broad definition, includes goal-oriented effort and "
        "overcoming difficulty, recognizes individual/collective and "
        "peaceful/nonviolent forms, and notes contextual valence."
    ),
    4: (
        "Correctly explains sustained effort toward a goal or overcoming "
        "hardship; includes at least one non-force dimension such as rights, "
        "progress, or change."
    ),
    3: (
        "Captures effort/struggle against difficulty but is somewhat narrow, "
        "repetitive, or misses collective/social change."
    ),
    2: (
        "Gives only a partial or overly physical meaning, such as fighting "
        "or defeating someone, without the broader sense of striving or resistance."
    ),
    1: "Wrong meaning, major factual/linguistic error, or irrelevant response.",
    0: (
        "No meaningful answer, refusal without reason, or response in the "
        "wrong language."
    ),
}


class Evaluator:
    """Validate and record a reviewer-assigned score using rubric version 1."""

    def evaluate_case(
        self,
        evaluation_id: str,
        input_text: str,
        expected_behavior: str,
        n_atlas_output: str,
        overall_score: Optional[int] = None,
        diagnostic_tags: Optional[Sequence[str]] = None,
        reviewer_rationale: Optional[str] = None,
        evaluation_method: str = "human_rubric_v1",
        timestamp: Optional[str] = None,
        system_version: Optional[str] = None,
    ) -> EvaluationRecord:
        """Record a human score from 0 to 5; no score is inferred by the code."""
        if not evaluation_id.strip():
            raise ValueError("evaluation_id must not be empty")
        if not input_text.strip():
            raise ValueError("input_text must not be empty")
        if not expected_behavior.strip():
            raise ValueError("expected_behavior must not be empty")
        if not n_atlas_output.strip():
            raise ValueError("n_atlas_output must not be empty")
        if not evaluation_method.strip():
            raise ValueError("evaluation_method must not be empty")
        if overall_score is None:
            raise ValueError("overall_score is required; provide a human rating from 0 to 5")
        if isinstance(overall_score, bool) or not isinstance(overall_score, int) or not 0 <= overall_score <= 5:
            raise ValueError("overall_score must be an integer from 0 to 5")

        tags = list(diagnostic_tags or [])
        diagnosis = (
            "reviewer_flagged_limitations" if tags else "no_issue_tagged_by_reviewer"
        )
        action = (
            "review_tagged_issues_and_re_evaluate"
            if tags
            else "retain_record_and_monitor"
        )
        context = f"; system_version={system_version}" if system_version else ""
        rationale = f"; rationale={reviewer_rationale}" if reviewer_rationale else ""
        method = (
            f"{evaluation_method}; score_label={SCORE_LABELS[overall_score]}"
            f"; score_description={SCORE_DESCRIPTIONS[overall_score]}"
            f"{rationale}{context}"
        )

        return EvaluationRecord(
            evaluation_id=evaluation_id,
            input=input_text,
            expected_behavior=expected_behavior,
            n_atlas_output=n_atlas_output,
            evaluation_method=method,
            score=float(overall_score),
            error_category=",".join(tags) if tags else None,
            diagnosis=diagnosis,
            improvement_action=action,
            timestamp=timestamp,
        )
