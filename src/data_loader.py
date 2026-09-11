"""Dataset loading utilities for the BrandSupportAI assignment.

This file is intentionally lightweight and reads a local CSV file if the user
has added the Kaggle-like customer support sample. It also falls back to a
small synthetic CSV record set so the repository remains runnable in a clean
clone without a full Kaggle download.
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable, List, Dict, Any


DEFAULT_DATASET = Path("data/customer_support_twitter.csv")


def load_csv(path: Path = DEFAULT_DATASET) -> List[Dict[str, Any]]:
    """Load a local CSV with a friendly fallback.

    Expected columns:
        tweet_id, brand, text, intent, reply, decision, reason
    """
    rows: List[Dict[str, Any]] = []
    if not path.exists():
        return build_local_sample_rows()

    with path.open("r", encoding="utf-8", newline="") as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            rows.append(row)

    return rows


def build_local_sample_rows() -> List[Dict[str, Any]]:
    """Create a compact sample row set for demonstration if CSV is not available."""
    return [
        {
            "tweet_id": "sample_001",
            "brand": "AppleSupport",
            "text": "My package is late and tracking still has no update.",
            "intent": "shipping_delay",
            "reply": "We are sorry your package is delayed. We will help track your order.",
            "decision": "auto_handle",
            "reason": "Clear shipping issue with a known support template.",
        },
        {
            "tweet_id": "sample_002",
            "brand": "AppleSupport",
            "text": "I was charged twice for my order and want a refund.",
            "intent": "billing_refund",
            "reply": "We are sorry about the duplicate charge. We will review the billing refund path.",
            "decision": "escalate",
            "reason": "Billing or refund require a human review path.",
        },
        {
            "tweet_id": "sample_003",
            "brand": "AppleSupport",
            "text": "I need help setting up my new device.",
            "intent": "product_setup",
            "reply": "We can help you set up the device step by step.",
            "decision": "auto_handle",
            "reason": "Issue is clear and can be solved by a guided reply.",
        },
    ]


def preview_rows(path: Path = DEFAULT_DATASET, limit: int = 5) -> List[Dict[str, Any]]:
    """Return a limited preview row set for the docs/demo files."""
    rows = load_csv(path)
    return rows[:limit]
