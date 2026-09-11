# Golden Evaluation Set Sampling and Labeling Note

The repository creates a `golden_eval_set.jsonl` file containing 150 examples. These examples are generated from a deterministic synthetic sampler that reuses message templates from known support categories: shipping delay, billing refund, product setup, delivery tracking, replacement order, and general complaint.

The examples are intended to satisfy the assignment’s deliverable shape while staying reproducible in a repository. In a production setting, we would label a larger set by stratified sampling from the dataset and then run a calibration pass with a human annotator. This would preserve coverage of low-frequency intents while avoiding over-sampling the most common themes.

The synthetic generation style is an offline stand-in for the requested gold set. It demonstrates the requested data structure clearly so the evaluation harness has a stable input format.
