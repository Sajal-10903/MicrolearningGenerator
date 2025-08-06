# transcriber.py
import os
import torch
import torchaudio
import uuid
from transformers import pipeline

device = "mps" if torch.backends.mps.is_available() else "cpu"
pipe = pipeline("automatic-speech-recognition", model="openai/whisper-base", device=device)

def transcribe_audio(mp3_path, video_id):  # ✅ Updated to accept video_id
    waveform, sample_rate = torchaudio.load(mp3_path)

    # convert waveform to mono and 16k
    waveform = waveform.mean(dim=0, keepdim=True)
    resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)
    waveform = resampler(waveform)

    audio_input = waveform.squeeze().numpy()
    result = pipe(audio_input)
    transcript = result["text"]

    output_dir = "lecture_notes"
    os.makedirs(output_dir, exist_ok=True)
    transcript_path = os.path.join(output_dir, f"{video_id}_transcript.txt")
    
    with open(transcript_path, "w", encoding="utf-8") as f:
        f.write(transcript)

    print(f"📝 Transcription saved: {transcript_path}")
    return transcript