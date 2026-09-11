# Data directory

This repository is intentionally structured to support the Hiver SDE Intern take-home assignment using a real customer support dataset.

## Expected datasets

The assignment references the public customer support dataset from Kaggle:

- `thoughtvector/customer-support-on-twitter`

A copy of the dataset should be placed here if you have local access to the Kaggle archive:

```text
data/customer_support_twitter.csv
```

For the optional intent extension, the taxonomy can be enriched using:

- `PolyAI/banking77` in Hugging Face style scope for a small intent taxonomy benchmark.

## Data use note

This workspace is an offline, reproducible starter pipeline. If the Kaggle archive is available locally, the dataset can be filtered to a single brand, such as AppleSupport or another selected brand, and then segmented into:

1. train/dev support examples
2. hand-labeled gold evaluation examples
3. escalation and routing label records

The raw dataset files are not included in this repository because the workspace does not contain the Kaggle archive and the repository must remain lightweight.
