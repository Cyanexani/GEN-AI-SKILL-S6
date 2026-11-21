# Week 2 - Provider-Agnostic LLM Client

`llm_client.py` defines a common `LLMProvider` interface with two providers: Gemini (cloud) and Ollama (local). `LLMClient` works with either one, so `main.py` can switch providers by name.

## Requirements
- Python 3.10+
- `google-genai`, `python-dotenv`, `requests`, `pytest` (see `../requirements.txt`)
- For Ollama: Ollama installed and running, with the model pulled (`ollama pull llama3.2`)
- A `.env` file in this folder (never committed):
  ```
  GEMINI_API_KEY=your_key_here
  GEMINI_MODEL=gemini-3.5-flash-lite
  OLLAMA_MODEL=llama3.2:latest
  ```

## Run
```powershell
pytest test_client.py   # unit test using a fake provider
python main.py          # type gemini or ollama, then your question
```
