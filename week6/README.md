# Week 6 - Golden Question Set and Baseline (Release v0.1)

`golden_set.json` holds 30 questions with expected answers, keywords and sources. `main.py` asks each question to Llama 3.2 through Ollama, scores each answer by keyword coverage (PASS at 60% or more, otherwise REVIEW), and saves the results to `baseline_results.csv`. This is the first baseline, labelled Release v0.1.

## Requirements
- Python 3.10+
- `requests` (see `requirements.txt`)
- Ollama installed and running, with the model pulled: `ollama pull llama3.2`
- No `.env` or API key needed

## Run
```powershell
python main.py
```
It takes a while on CPU, about a minute per question.
