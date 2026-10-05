from __future__ import annotations

from argparse import ArgumentParser

from llm_eval_kit.evaluator import Evaluator
from llm_eval_kit.models import PromptCase


def main() -> None:
    parser = ArgumentParser(description="Evaluate model responses against prompt cases.")
    parser.add_argument("--prompt", default="Summarize the benefits of local-first AI.")
    parser.add_argument("--keywords", nargs="*", default=["privacy", "latency", "control"])
    args = parser.parse_args()

    case = PromptCase(
        id="demo-case",
        prompt=args.prompt,
        expected_keywords=args.keywords,
    )
    evaluator = Evaluator()
    results = evaluator.evaluate_cases([case], ["Local-first AI improves privacy, reduces latency, and gives users more control over their data."])
    print(results[0])


if __name__ == "__main__":
    main()
