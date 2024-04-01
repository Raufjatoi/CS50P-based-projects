import pyttsx3
from pydub import AudioSegment
from pydub.playback import play

def text_to_speech_with_beat(text, beat_file):
    # Initialize text-to-speech engine
    engine = pyttsx3.init()

    # Convert text to speech and save to a temporary file
    engine.save_to_file(text, "temp_speech.wav")
    engine.runAndWait()

    # Load the speech audio file
    speech = AudioSegment.from_wav("temp_speech.wav")

    # Load the beat audio file
    beat = AudioSegment.from_mp3(beat_file)

    # Adjust the duration of speech to match the beat
    speech = speech.set_duration(len(beat))

    # Overlay speech onto the beat
    combined = beat.overlay(speech)

    # Play the combined audio
    play(combined)

# Example usage
text = "Hello, I'm a Rauf, weird dude, just a uni student, never playing it cool"
beat_file = "txt to speach and sound/1.mp3"  # Replace with the path to your beat audio file
text_to_speech_with_beat(text, beat_file)
