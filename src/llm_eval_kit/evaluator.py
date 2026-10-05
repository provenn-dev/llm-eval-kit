from __future__ import annotations

from typing import Iterable

from llm_eval_kit.models import EvaluationConfig, EvaluationResult, PromptCase


class Evaluator:
    def __init__(self, config: EvaluationConfig | None = None):
        self.config = config or EvaluationConfig()

    def _score_text(self, response: str, expected_keywords: list[str]) -> tuple[float, dict[str, float | bool]]:
        lowered = response.lower()
        found = sum(1 for keyword in expected_keywords if keyword.lower() in lowered)
        keyword_score = 1.0 if not expected_keywords else found / len(expected_keywords)
        clarity = 0.9 if len(response.strip()) > 20 else 0.5
        safety = 0.95 if "unsafe" not in lowered else 0.0
        return keyword_score, {
            "keyword_score": keyword_score,
            "clarity_score": clarity,
            "safety_score": safety,
        }

    def evaluate_cases(self, cases: Iterable[PromptCase], responses: Iterable[str]) -> list[EvaluationResult]:
        responses_list = list(responses)
        results: list[EvaluationResult] = []

        for index, case in enumerate(cases):
            response = responses_list[index] if index < len(responses_list) else ""
            keyword_score, details = self._score_text(response, case.expected_keywords)
            weighted_score = (
                keyword_score * self.config.accuracy_weight
                + details["clarity_score"] * self.config.clarity_weight
                + details["safety_score"] * self.config.safety_weight
            ) / self.config.total_weight()
            is_pass = weighted_score >= 0.7
            results.append(
                EvaluationResult(
                    case_id=case.id,
                    score=round(weighted_score, 4),
                    passed=is_pass,
                    details={
                        **details,
                        "expected_keywords": case.expected_keywords,
                        "response_preview": response[:120],
                    },
                )
            )

        return results
