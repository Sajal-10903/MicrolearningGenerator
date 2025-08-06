# summarizer.py
def summarize_text(text, llm):
    prompt = (
        "You're a helpful assistant. Summarize the key points of the following lecture:\n\n"
        f"{text}\n\nSummary:"
    )
    return llm.predict(prompt)