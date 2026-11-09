import numpy as np
import sounddevice as sd
import soundfile as sf
import os 
import config.input_setting as in_set ; 
def get_audio_devices():
    #Get a list of available audio input devices.
    devices = sd.query_devices()
    input_devices = [device for device in devices if device['max_input_channels'] > 0 ]
    return input_devices
def record_audio(duration):
    #Record audio from chosen input device
     
    audio_data = sd.rec(
        frames=duration * in_set.SAMPLE_RATE,
        samplerate=in_set.SAMPLE_RATE,
        channels=in_set.CHANNELS,
        dtype=in_set.AUDIO_DTYPE,
    )
    sd.wait()
    return audio_data
def create_output_directory(directory):
    #Create output directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)
def get_output_file_path(directory, filename):
    #Get the full path for the output file
    create_output_directory(directory)
    filename_directory = os.path.join(directory, filename)
    return filename_directory
def save_audio_to_file(audio_data,filename,directory="recorded_audio"):
    #save the recorded audio to .wav file
    filename_path = get_output_file_path(directory, filename)
    sf.write(filename_path, audio_data, in_set.SAMPLE_RATE, subtype='PCM_16')



