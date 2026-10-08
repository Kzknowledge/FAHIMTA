"""System-agnostic evaluation boundary for the MVP."""

from typing import Protocol

from .models import EvaluationRecord


class NAtlasAdapter(Protocol):
    """Minimal adapter boundary for an actual N-ATLAS integration."""

    def evaluate(self, input_text: str) -> str:
        """Return the target system's response for an input."""
        ...


class Evaluator:
    """Apply a documented evaluation procedure to a target-system response."""

    def evaluate_case(
        self,
        evaluation_id: str,
        input_text: str,
        expected_behavior: str,
        n_atlas_output: str,
    ) -> EvaluationRecord:
        raise NotImplementedError(
            "MVP evaluator logic will be implemented after the evaluation metric "
            "and N-ATLAS interface are verified."
        )