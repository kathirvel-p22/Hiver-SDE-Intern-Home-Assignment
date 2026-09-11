# BrandSupportAI Support Agent Report

## Problem framing

For this assignment, the target brand is AppleSupport. A good support agent should understand customer needs, respond in a style consistent with historical brand support messages, and make a safe routing decision between auto-handle and human escalation. We intentionally limit the scope to a single brand and a compact set of intents. We do not build an end-to-end customer conversation memory system or a generic multi-brand multi-language model.

## What is good enough to trust?

A good local system must: (1) label the incoming message into a stable intent; (2) draft a concise reply grounded in the brand response style; and (3) either auto-handle or escalate with an auditable reason. The system also needs to demonstrate when it is uncertain.

## Baselines

1. Trivial baseline: classify every message as `general_complaint` and use a generic response.
2. Simple baseline: keyword-only labeler using shipping and refund signal terms.

Our deterministic heuristic classifier improves on the trivial baseline by creating a more consistent set of intents and better reply grounding. It also keeps system behavior transparent and reproducible.

## Results

The generated offline evaluation uses 150 synthetic tasks. Evaluation output is stored in `results/evaluation_report.json`. The benchmark uses offline metrics: accuracy, macro F1, and an LLM-as-judge proxy rubric. The headline result is that the evaluation harness reports `accuracy` and `macro_f1` above a minimum threshold.

## Failure analysis

1. `Shipping delay` and `delivery tracking` messages may be confused because both contain `delivery`, `order`, and `tracking` terms.
2. `Billing_refund` can be mistaken for `general_complaint` when the complaint is only phrased as a charge problem.
3. `Product_setup` can be mistaken for `general_complaint` when the customer complains about installation or app access.
4. Confidence is low when the message is too short or has mixed signals.
5. Edge cases involving fraud, account security, and threats require escalation.

## What is misleading about my headline number?

Headline numbers can look stronger than they are because this repository uses a deterministic, synthetic sample instead of a full human-labeled real-world dataset. The evaluation harness does not use a production LLM cost model, and the golden set is a purpose-built sample rather than a comprehensive benchmark. The generated metrics are best viewed as proof-of-workshop demonstrators rather than a final production claim.

## What I would do next with one more week

1. Expand the golden set to include 200+ real examples sampled from the public support dataset.
2. Use a semantically grounded model or prompt-based LLM judge with calibrated agreement checks.
3. Add real answer evidence retrieval from a brand response history database.
4. Build a human-in-the-loop escalation interface and richer intent taxonomy.
5. Add a realistic open-source dataset preprocessing pipeline.

## Summary

This repository demonstrates a credible, reproducible, single-brand support AI concept that can be run locally and evaluated with offline metrics. It is intentionally compact so that the README and scripts fit the assignment’s short-turnaround constraints.
