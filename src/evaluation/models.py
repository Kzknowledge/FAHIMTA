"""Core MVP data structures."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class EvaluationRecord:
    evaluation_id: str
    input: str
    expected_behavior: Optional[str] = None
    n_atlas_output: Optional[str] = None
    evaluation_method: Optional[str] = None
    score: Optional[float] = None
    error_category: Optional[str] = None
    diagnosis: Optional[str] = None
    improvement_action: Optional[str] = None
    re_evaluation_result: Optional[str] = None
    timestamp: Optional[str] = None
    version: str = "0.1.0"