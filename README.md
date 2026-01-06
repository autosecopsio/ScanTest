# Scanner Test Repository

⚠️ This repository is intentionally insecure and contains fake secrets
used ONLY for testing secret-scanning tools.

## Purpose
Validate that a scanner can:
- Detect real-looking leaked secrets
- Ignore false positives
- Handle tricky and real-world edge cases

## Expected Results

| Folder            | Expected Outcome |
|-------------------|------------------|
| clean/            | No findings      |
| obvious_secrets/  | High severity    |
| false_positives/  | No findings      |
| tricky_cases/     | Medium/High      |
| mixed/            | Multiple findings|

All keys are fake and safe.
