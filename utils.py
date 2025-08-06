import os
import shutil

def clear_downloads():
    folder = "downloads"
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.makedirs(folder)
    print("🧹 Old downloads cleaned.")

def save_text(content, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"💾 Saved: {file_path}")