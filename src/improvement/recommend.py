"""Improvement recommendation boundary."""


def recommend(diagnosis: str) -> str:
    """Map a diagnosis to a conservative next action."""
    if diagnosis == "no_failure_detected":
        return "no_intervention"
    return "review_case_and_define_targeted_intervention"
