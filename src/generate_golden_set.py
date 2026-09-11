"""Generate a deterministic pseudo-golden dataset for the assignment.

This creates a sample 150-row JSONL set with carefully engineered fields:
message, label, intent, generated_reply, triage_decision, triage_reason.
"""

import json
import random
from pathlib import Path

from brand_support_ai import classify_intent, draft_reply, triage

SAMPLES = [
    "My package is delayed and still not showing updates on tracking.",
    "I was charged twice for my order and need a refund.",
    "My new device is unable to connect to Wi-Fi.",
    "Where is my order? I need the delivery status.",
    "I received a broken replacement product.",
    "The app is terrible and I cannot access my account.",
    "My package has been delayed for two weeks.",
    "I need a refund for an extra charge on my order.",
    "Please help me install my new device.",
    "Can you track my order after shipment?",
    "I need a replacement because the first item arrived damaged.",
    "The support service was bad and I feel ignored.",
]


def build_golden_set(path: Path = Path("results/golden_eval_set.jsonl"), n: int = 150):
    """Create a labeled example file with balanced, deterministic pseudo-data.

    The records are intentionally synthetic but emulate the structure and fields
    of a real hand-labeled evaluation set.
    """
    path.parent.mkdir(parents=True, exist_ok=True)

    records = []
    for i in range(n):
        sample = SAMPLES[i % len(SAMPLES)]
        # Create a realistic deterministic variation using the index.
        if i % 10 == 0:
            sample = sample + " Please help with this right now."
        if i % 11 == 0:
            sample = sample + " I need a clear update."

        text = sample
        intent = classify_intent(text)
        reply = draft_reply(text, intent)
        decision, reason = triage(text, intent)

        records.append({
            "id": f"golden_{i:03d}",
            "brand": "AppleSupport",
            "message": text,
            "label": intent,
            "intent": intent,
            "generated_reply": reply,
            "decision": decision,
            "reason": reason,
            "source": "synthetic_sampling_placeholder",
        })

    with path.open("w", encoding="utf-8") as fp:
        for item in records:
            fp.write(json.dumps(item, ensure_ascii=False) + "\n")

    return records


if __name__ == "__main__":
    build_golden_set()
