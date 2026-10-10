import pytest

from src.evaluation.evaluator import SCORE_LABELS, Evaluator


def _evaluate(score, **kwargs):
    return Evaluator().evaluate_case(
        evaluation_id="TEST-EXAMPLE",
        input_text="Menene ake nufi da gwagwarmaya?",
        expected_behavior="Broadly explain struggle, goal-oriented effort, and context.",
        n_atlas_output="A recorded sample response.",
        overall_score=score,
        **kwargs,
    )


@pytest.mark.parametrize(
    ("score", "label"),
    [(0, "Unusable"), (1, "Poor"), (2, "Weak"),
     (3, "Adequate"), (4, "Strong"), (5, "Excellent")],
)
def test_all_rubric_scores_are_recorded(score, label):
    record = _evaluate(score, reviewer_rationale="Example test rationale")
    assert record.score == float(score)
    assert f"score_label={label}" in record.evaluation_method
    assert label == SCORE_LABELS[score]


def test_test001_human_judgement_can_be_recorded_without_reinventing_ratings():
    record = _evaluate(
        3,
        diagnostic_tags=[
            "semantic-narrowing",
            "confrontation-overemphasis",
            "omitted-collective-scope",
            "omitted-rights-and-social-change",
            "non-force-methods-underrepresented",
        ],
        reviewer_rationale="Broadly correct but semantically narrow.",
        timestamp="2026-10-10",
        system_version="unverified-demo",
    )
    assert record.score == 3.0
    assert record.diagnosis == "reviewer_flagged_limitations"
    assert "Adequate" in record.evaluation_method
    assert "unverified-demo" in record.evaluation_method


def test_evaluator_requires_explicit_human_score():
    with pytest.raises(ValueError, match="overall_score is required"):
        Evaluator().evaluate_case(
            evaluation_id="TEST-EMPTY",
            input_text="input",
            expected_behavior="expected",
            n_atlas_output="output",
        )


@pytest.mark.parametrize("score", [-1, 6, 1.5, True, "3"])
def test_evaluator_rejects_invalid_scores(score):
    with pytest.raises(ValueError, match="integer from 0 to 5"):
        _evaluate(score)


def test_evaluator_rejects_blank_required_text():
    with pytest.raises(ValueError, match="input_text"):
        Evaluator().evaluate_case(
            evaluation_id="TEST-BLANK",
            input_text=" ",
            expected_behavior="expected",
            n_atlas_output="output",
            overall_score=3,
        )
