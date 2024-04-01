from pydub import AudioSegment

def mix_audio_files(speech_file, beat_file, output_file):
    # Load speech and beat audio files
    speech = AudioSegment.from_file(speech_file)
    beat = AudioSegment.from_file(beat_file)

    # Adjust the duration of the beat to match the duration of the speech (if necessary)
    if len(beat) < len(speech):
        beat = beat * (len(speech) // len(beat)) + beat[:len(speech) % len(beat)]
    elif len(beat) > len(speech):
        beat = beat[:len(speech)]

    # Mix speech with beat
    mixed_audio = speech.overlay(beat)

    # Export the mixed audio to MP3 format
    mixed_audio.export(output_file, format="mp3")

    print("Mixed audio saved successfully.")

# Example usage
speech_file = "txt to speach and sound/temp_speech.wav"  # Update the path to your WAV speech file
beat_file = "1.mp3"  # Update the path to your MP3 beat file
output_file = "mixed_audio.mp3"

mix_audio_files(speech_file, beat_file, output_file)
