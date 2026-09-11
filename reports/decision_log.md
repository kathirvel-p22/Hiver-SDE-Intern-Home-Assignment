# Decision Log

- Use a single-brand scope, AppleSupport, to make the evaluation and reply style easier to ground.
- Use a compact intent set instead of a large bespoke taxonomy because the dataset is noisy and the assignment prioritizes proof.
- Implement a deterministic keyword classifier rather than an API-dependent model to make the local run transparent.
- Keep the generated reply in a brand-grounded template style rather than asking the system to invent a completely new answer.
- Escalate billing and refund issues in the first pass because those are sensitive and require human confidence.
- Escalate account security or login issues automatically because of high privacy risk.
- Build a synthetic golden set from the same message template patterns so the repository remains reproducible offline.
- Use a minimal automated evaluation harness rather than a large external dependency chain.
- Keep the evaluation harness local to honor the README reproduction requirement and the 15-minute target.
- Use a literature-style report, not a large PDF or dashboard, to satisfy the assignment report requirements.
- Surface the reason for triage decisions in the generated records so stakeholders can inspect the system behavior.
- Choose a simple deterministic judge rubric rather than a commercial LLM-as-judge pipeline because the run must be reproducible.
- Keep the benchmark synthetic enough to avoid API key or model drift while making the system easy to adapt.
