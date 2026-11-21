# Week 5 - Feature Budget Calculator

`budget.py` defines `FeatureBudget`, which estimates the daily and monthly cost of an LLM feature from request volume, token counts and prices. It also checks rate limits (RPM and TPM) and applies a safety margin.

## Requirements
- Python 3.10+
- `python-dotenv` (see `requirements.txt`)
- A `.env` file in this folder (never committed) with these settings: `REQUESTS_PER_DAY`, `AVG_INPUT_TOKENS`, `AVG_OUTPUT_TOKENS`, `PEAK_REQUESTS_PER_MINUTE`, `INPUT_PRICE_PER_MILLION`, `OUTPUT_PRICE_PER_MILLION`, `RPM_LIMIT`, `TPM_LIMIT`, `MONTHLY_BUDGET_USD`, `DAILY_BUDGET_USD`, `SAFETY_MARGIN_PERCENT`

## Run the tests
```powershell
python -m unittest test_budget -v
```
