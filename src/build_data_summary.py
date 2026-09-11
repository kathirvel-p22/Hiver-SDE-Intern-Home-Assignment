"""Create a small sample data summary report for the assignment.

This is a local data proof step that can run without the Kaggle archive.
"""

from pathlib import Path
import json

from data_loader import load_csv, preview_rows


def build_summary(path: Path = Path("data/customer_support_twitter.csv")) -> dict:
    rows = load_csv(path)
    brands = {}
    intents = {}
    for row in rows:
        brand = (row.get("brand") or "Unknown").strip()
        intent = (row.get("intent") or row.get("label") or "unknown").strip()
        brands[brand] = brands.get(brand, 0) + 1
        intents[intent] = intents.get(intent, 0) + 1

    return {
        "rows": len(rows),
        "brands": brands,
        "intent_counts": intents,
        "preview": preview_rows(path, limit=5),
    }


if __name__ == "__main__":
    output = build_summary()
    out = Path("results/data_summary.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(json.dumps(output, indent=2))
