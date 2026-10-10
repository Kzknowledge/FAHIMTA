import pytest

from src.evaluation.evaluator import DEFAULT_DIMENSIONS, Evaluator


def test_evaluator_computes_mean_of_reviewer_ratings():
    ratings = {
        "core_meaning": 4,
        "goal_orientation": 3,
        "individual_and_collective_scope": 2,
        "non_force_methods": 2,
        "contextual_valence": 4,
    }
    record = Evaluator().evaluate_case(
        evaluation_id="TEST-EXAMPLE",
        input_text="What does gwagwarmaya mean?",
        expected_behavior="Explain struggle broadly, including non-force meanings.",
        n_atlas_output="A sample recorded response.",
        rubric_scores=ratings,
        diagnostic_tags=["semantic-narrowing"],
        timestamp="2026-10-10",
        system_version="unverified-demo",
    )

    assert record.score == 3.0
    assert record.error_category == "semantic-narrowing"
    assert record.diagnosis == "reviewer_flagged_limitations"
    assert "human_rubric_v1" in record.evaluation_method
    assert "unverified-demo" in record.evaluation_method


def test_evaluator_requires_explicit_reviewer_ratings():
    with pytest.raises(ValueError, match="rubric_scores are required"):
        Evaluator().evaluate_case(
            evaluation_id="TEST-EMPTY",
            input_text="input",
            expected_behavior="expected",
            n_atlas_output="output",
        )


@pytest.mark.parametrize("rating", [0, 6, 1.5, True, "4"])
def test_evaluator_rejects_invalid_ratings(rating):
    ratings = {dimension: 3 for dimension in DEFAULT_DIMENSIONS}
    ratings["core_meaning"] = rating

    with pytest.raises(ValueError, match="integer from 1 to 5"):
        Evaluator().evaluate_case(
            evaluation_id="TEST-INVALID",
            input_text="input",
            expected_behavior="expected",
            n_atlas_output="output",
            rubric_scores=ratings,
        )


def test_evaluator_rejects_missing_required_text():
    with pytest.raises(ValueError, match="input_text"):
        Evaluator().evaluate_case(
            evaluation_id="TEST-BLANK",
            input_text="  ",
            expected_behavior="expected",
            n_atlas_output="output",
            rubric_scores={"core_meaning": 3},
        )
