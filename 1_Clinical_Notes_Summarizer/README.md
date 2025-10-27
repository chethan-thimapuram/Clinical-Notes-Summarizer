# Clinical Notes Summarizer (Demo)

Demo FastAPI service that uses a small Transformer summarization model (t5-small) to summarize clinical text.

## Run locally (demo)
1. create a virtualenv and install requirements:
   ```bash
   python -m venv venv
   source venv/bin/activate   # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```
2. Start the server:
   ```bash
   uvicorn app:app --reload --port 8000
   ```
3. Test with curl / Postman:
   ```bash
   curl -X POST http://127.0.0.1:8000/summarize/ -H 'Content-Type: application/json' -d '{ "text": "Patient presented with cough and fever ..." }'
   ```
