from faster_whisper import WhisperModel
from config.stt_setting import beamsize, vad_filter, condition_on_previous_text ,english_only
def load_model(model_size="small",device="cuda", compute_type="float16"):
    return WhisperModel(model_size, device=device, compute_type=compute_type)

def transcribe_audio(model, audio_path):
    segments, info = model.transcribe(audio_path, beam_size=beamsize, vad_filter=vad_filter, condition_on_previous_text=condition_on_previous_text, language="en" if english_only else None)
    transcription = ""
    for segment in segments:
        transcription += segment.text + " "
    return transcription.strip()