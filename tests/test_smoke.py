from src.diagnosis.diagnose import diagnose
from src.improvement.recommend import recommend


def test_diagnosis_and_recommendation_smoke():
    diagnosis = diagnose(score=0.8, threshold=0.7)
    assert diagnosis == "no_failure_detected"
    assert recommend(diagnosis) == "no_intervention"


def test_failure_path_smoke():
    diagnosis = diagnose(score=0.4, threshold=0.7)
    assert diagnosis == "evaluation_failure"
    assert recommend(diagnosis) == "review_case_and_define_targeted_intervention"