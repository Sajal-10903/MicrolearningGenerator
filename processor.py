from transformers import pipeline

# Load locally cached summarizer and Q&A models
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def summarize_text(text):
    max_chunk_size = 1000
    chunks = [text[i:i+max_chunk_size] for i in range(0, len(text), max_chunk_size)]
    summarized_chunks = []

    for chunk in chunks:
        summary = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
        summarized_chunks.append(summary[0]['summary_text'])

    return "\n".join(summarized_chunks)

def generate_flashcards(text):
    context = text[:4000]  # reduce context to stay within model limits
    questions = [
        "What is the main topic discussed?",
        "List one key insight mentioned.",
        "What is an example given in the text?",
        "What is the conclusion or takeaway?"
    ]

    flashcards = []
    for q in questions:
        try:
            answer = qa_pipeline(question=q, context=context)
            flashcards.append({
                "question": q,
                "answer": answer['answer']
            })
        except Exception as e:
            flashcards.append({
                "question": q,
                "answer": "Could not generate answer."
            })

    return flashcards