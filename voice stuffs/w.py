import whisper

model = whisper.load_model("base")  # Load other models like "small", "medium", etc., if needed

# Transcribe audio file
result = model.transcribe("audio.mp3")
print(result["text"])
