"""Diagnosis boundary for classifying evaluation failures."""


def diagnose(*, score: float, threshold: float) -> str:
    """Return a minimal, deterministic diagnosis from an explicit threshold."""
    if score >= threshold:
        return "no_failure_detected"
    return "evaluation_failure"
