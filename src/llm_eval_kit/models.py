from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Iterable


@dataclass
class PromptCase:
    id: str
    prompt: str
    expected_keywords: list[str] = field(default_factory=list)
    expected_response: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class EvaluationResult:
    case_id: str
    score: float
    passed: bool
    details: dict[str, Any] = field(default_factory=dict)


@dataclass
class EvaluationConfig:
    accuracy_weight: float = 0.6
    clarity_weight: float = 0.25
    safety_weight: float = 0.15

    def total_weight(self) -> float:
        return self.accuracy_weight + self.clarity_weight + self.safety_weight
