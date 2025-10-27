from fastapi import FastAPI, Request
from transformers import pipeline

app = FastAPI(title="Clinical Notes Summarizer (Demo)")

# Demo model: lightweight summarizer (uses t5-small by default)
summarizer = pipeline("summarization", model="t5-small")

@app.post("/summarize/")
async def summarize_text(request: Request):
    data = await request.json()
    text = data.get("text", "")
    if not text:
        return {"error": "No text provided"}
    summary = summarizer(text, max_length=120, min_length=30, do_sample=False)
    return {"summary": summary[0]['summary_text']}
