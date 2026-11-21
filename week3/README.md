# Week 3 - API Usage Monitoring

Calls Gemini and logs each request (model, prompt, response, token estimates, latency, status) to MongoDB. `database.py` connects to MongoDB, and `monitoring.py` holds the logging helpers.

## Requirements
- Python 3.10+
- `google-genai`, `python-dotenv`, `pymongo` (see `../requirements.txt`)
- A reachable MongoDB (for example Atlas, with your IP allowed)
- A `.env` file in this folder (never committed):
  ```
  GEMINI_API_KEY=your_key_here
  MONGODB_URI=your_mongodb_connection_string
  ```

## Run
```powershell
python main.py
```
