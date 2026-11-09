from audio_input.microphone import get_audio_devices , record_audio, save_audio_to_file 
from speech_to_text.whisper import load_model, transcribe_audio
import keyboard as kb
def main():
    devices = get_audio_devices()
    model = load_model("small")
    # Record audio for 5 seconds
    audio_data = record_audio(5)

    # Save audio to output.wav
    save_audio_to_file(audio_data, "output.wav")
    print("Audio recorded successfully!")
    transcription = transcribe_audio(model, "recorded_audio/output.wav")
    print("Transcription:", transcription)

if __name__ == "__main__":
    main()