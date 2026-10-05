# llm-eval-kit

A practical toolkit for evaluating prompts, comparing model outputs, and running lightweight AI/LLM experiments locally.

## Why this project exists

LLM quality is difficult to judge with ad hoc prompting alone. This project gives teams a repeatable way to:

- define evaluation cases
- compare model responses across providers or local backends
- score outputs with deterministic criteria
- track regressions over time

## Features

- prompt case definitions with expected behaviors
- scoring rubric for accuracy, clarity, and safety
- comparison utilities for multiple models or runs
- CLI entry point for local experimentation

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
llm-eval --help
```

## Example

```python
from llm_eval_kit.models import PromptCase
from llm_eval_kit.evaluator import Evaluator

cases = [
    PromptCase(
        id="q1",
        prompt="Summarize the benefits of local-first AI.",
        expected_keywords=["privacy", "latency", "control"],
    )
]

results = Evaluator().evaluate_cases(cases, ["Response 1", "Response 2"])
print(results)
```

## Roadmap

- local prompt benchmark runner
- CSV/JSON export for results
- provider adapters for Ollama, OpenAI, and Hugging Face
- regression dashboard and trend reporting
