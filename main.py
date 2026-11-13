from action_tools.tool_registry import execute_tool
from audio_input.microphone import get_audio_devices , record_audio, save_audio_to_file 
from speech_to_text.whisper import load_model, transcribe_audio
from command.commands_router import command_router
def main():

    # devices = get_audio_devices()
    # model = load_model("large-v3-turbo", device="cuda", compute_type="int8_float16")
    # # Record audio for 5 seconds
    # print("Starting recording...")
    # audio_data = record_audio(5)

    # # Save audio to output.wav
    # save_audio_to_file(audio_data, "output.wav")
    # print("Audio recorded successfully!")
    # transcription = transcribe_audio(model, "recorded_audio/output.wav")
    #print("Transcription:", transcription)
    transcription = ""
    command_router(transcription)
    
if __name__ == "__main__":
    main()