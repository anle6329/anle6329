from faster_whisper import WhisperModel
def load_model(model_size="small"):
    return WhisperModel(model_size, device="cuda", compute_type="float16")
def transcribe_audio(model, audio_path):
    segments, info = model.transcribe(audio_path, beam_size=5)
    transcription = ""
    for segment in segments:
        transcription += segment.text + " "
    return transcription.strip()