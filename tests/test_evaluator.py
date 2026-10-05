from __future__ import annotations

from llm_eval_kit.evaluator import Evaluator
from llm_eval_kit.models import EvaluationConfig, PromptCase


def test_evaluator_scores_expected_keywords() -> None:
    case = PromptCase(
        id="case-1",
        prompt="Summarize local-first AI benefits.",
        expected_keywords=["privacy", "latency", "control"],
    )
    response = "Local-first AI improves privacy, cuts latency, and gives users more control."
    result = Evaluator(EvaluationConfig()).evaluate_cases([case], [response])[0]

    assert result.passed is True
    assert result.score > 0.7
    assert result.details["keyword_score"] == 1.0
