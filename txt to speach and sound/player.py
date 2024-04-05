import soundfile as sf
import numpy as np

# Load the audio files
wave_data, wave_samplerate = sf.read("txt to speach and sound/sing.wav")
mp3_data, mp3_samplerate = sf.read("txt to speach and sound/sing.mp3")

# Convert both audio files to mono if they have more than one channel
if len(wave_data.shape) > 1 and wave_data.shape[1] > 1:
    wave_data = np.mean(wave_data, axis=1)
if len(mp3_data.shape) > 1 and mp3_data.shape[1] > 1:
    mp3_data = np.mean(mp3_data, axis=1)

# Adjust the length of the shorter audio to match the longer one
min_length = min(len(wave_data), len(mp3_data))
wave_data = wave_data[:min_length]
mp3_data = mp3_data[:min_length]

# Mix the audio files
mixed_data = np.array(wave_data) + np.array(mp3_data)

# Normalize the mixed audio data to prevent clipping
mixed_data /= np.max(np.abs(mixed_data))

# Save the mixed audio to a new wave file
sf.write("mixed_audio.wav", mixed_data, wave_samplerate)
