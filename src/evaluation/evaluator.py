"""Transparent rubric-based evaluation for recorded model outputs.

This module does not infer semantic quality automatically. A reviewer supplies
dimension ratings; FAHIMTA validates the ratings, computes a transparent mean,
and records the evidence and limitations.
"""
from typing import Mapping, Optional, Protocol, Sequence

from .models import EvaluationRecord


class NAtlasAdapter(Protocol):
    """Minimal adapter boundary for an actual N-ATLAS integration."""

    def evaluate(self, input_text: str) -> str:
        """Return the target system's response for an input."""
        ...


DEFAULT_DIMENSIONS = (
    "core_meaning",
    "goal_orientation",
    "individual_and_collective_scope",
    "non_force_methods",
    "contextual_valence",
)


class Evaluator:
    """Create a structured record from reviewer-provided rubric ratings."""

    def evaluate_case(
        self,
        evaluation_id: str,
        input_text: str,
        expected_behavior: str,
        n_atlas_output: str,
        rubric_scores: Optional[Mapping[str, int]] = None,
        diagnostic_tags: Optional[Sequence[str]] = None,
        evaluation_method: str = "human_rubric_v1",
        timestamp: Optional[str] = None,
        system_version: Optional[str] = None,
    ) -> EvaluationRecord:
        """Validate 1–5 ratings and record their arithmetic mean.

        Ratings must be supplied by a human reviewer; they are not inferred
        from the text. The mean is descriptive and is not a probability,
        model-accuracy estimate, or statistically validated benchmark score.
        """
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
        if not rubric_scores:
            raise ValueError(
                "rubric_scores are required; FAHIMTA does not automatically "
                "infer semantic quality"
            )

        unknown = set(rubric_scores) - set(DEFAULT_DIMENSIONS)
        if unknown:
            raise ValueError(f"Unknown rubric dimensions: {sorted(unknown)}")
        if not set(rubric_scores).issubset(DEFAULT_DIMENSIONS):
            raise ValueError("Invalid rubric dimensions")
        for dimension, rating in rubric_scores.items():
            if isinstance(rating, bool) or not isinstance(rating, int) or not 1 <= rating <= 5:
                raise ValueError(f"{dimension} must be an integer from 1 to 5")

        # Score is the unrounded arithmetic mean of reviewer-entered ratings.
        score = sum(rubric_scores.values()) / len(rubric_scores)
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
        method = f"{evaluation_method}; ratings={dict(rubric_scores)}{context}"

        return EvaluationRecord(
            evaluation_id=evaluation_id,
            input=input_text,
            expected_behavior=expected_behavior,
            n_atlas_output=n_atlas_output,
            evaluation_method=method,
            score=score,
            error_category=",".join(tags) if tags else None,
            diagnosis=diagnosis,
            improvement_action=action,
            timestamp=timestamp,
        )
