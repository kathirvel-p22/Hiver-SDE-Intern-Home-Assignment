"""Small end-to-end example runner for the BrandSupportAI assignment."""

import json
from pathlib import Path

from brand_support_ai import process_message


def run_demo(messages=None):
    messages = messages or [
        "My package is late and I still have no tracking update.",
        "I was charged twice and need a refund now.",
        "I need help connecting my device to Wi-Fi.",
    ]

    results = []
    for msg in messages:
        output = process_message(msg)
        results.append(output)

    out = Path("results/demo_run.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(results, indent=2), encoding="utf-8")
    return results


if __name__ == "__main__":
    print(json.dumps(run_demo(), indent=2))
