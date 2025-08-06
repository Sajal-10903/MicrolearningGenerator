# flashcard_generator.py
def generate_flashcards(text, llm):
    prompt = (
        "From the following lecture transcript, generate 5 flashcards in Q&A format:\n\n"
        f"{text}\n\nFlashcards:"
    )
    response = llm.predict(prompt)
    
    flashcards = []
    lines = response.strip().split("\n")
    question, answer = None, None
    for line in lines:
        if line.strip().lower().startswith("q:"):
            question = line.split(":", 1)[1].strip()
        elif line.strip().lower().startswith("a:"):
            answer = line.split(":", 1)[1].strip()
            if question and answer:
                flashcards.append((question, answer))
                question, answer = None, None
    return flashcards