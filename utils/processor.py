import os
from transformers import pipeline
import nltk
from nltk.tokenize import sent_tokenize

# Download NLTK data for sentence tokenization
nltk.download('punkt_tab')

# Initialize BART summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    try:
        # Tokenize text into sentences
        sentences = sent_tokenize(text)
        # BART model max input length ~1024 tokens, so truncate if needed
        input_text = " ".join(sentences[:min(len(sentences), 50)])  # Limit to 50 sentences
        input_text = input_text[:4000]  # Truncate to ~4000 chars to avoid token limit
        
        # Summarize using BART
        summary = summarizer(input_text, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
        return summary.strip()
    except Exception as e:
        raise RuntimeError(f"❌ Summarization failed: {e}")

def generate_flashcards(text, video_id):
    try:
        # Simple rule-based flashcard generation using sentence importance
        sentences = sent_tokenize(text)
        # Select top 5 sentences (basic approach, can be improved with TF-IDF or embeddings)
        selected_sentences = sentences[:min(len(sentences), 5)]
        
        flashcards = []
        for i, sentence in enumerate(selected_sentences):
            # Create simple Q&A (this can be improved with better question generation)
            question = f"What is a key point {i+1} from the lecture?"
            answer = sentence.strip()
            flashcards.append((question, answer))
        
        # Save flashcards
        output_dir = "flashcards"
        os.makedirs(output_dir, exist_ok=True)
        flashcard_path = os.path.join(output_dir, f"{video_id}_flashcards.txt")
        with open(flashcard_path, "w") as f:
            for q, a in flashcards:
                f.write(f"Q: {q}\nA: {a}\n\n")
        print(f"💾 Saved: {flashcard_path}")
        return flashcards
    except Exception as e:
        raise RuntimeError(f"❌ Flashcard generation failed: {e}")