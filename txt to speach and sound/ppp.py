import pyttsx3

def generate_and_save_voice(text, output_file):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties for the UK English voice
    voices = engine.getProperty('voices')
    uk_voice = None
    for voice in voices:
        if voice.languages and "english" in voice.languages[0].lower() and "uk" in voice.name.lower():
            uk_voice = voice
            break
    if uk_voice:
        engine.setProperty('voice', uk_voice.id)

    # Set medium speed
    engine.setProperty('rate', 150)  # Adjust as needed

    # Generate the voice for the given text
    engine.save_to_file(text, output_file)

    # Run the engine
    engine.runAndWait()

if __name__ == "__main__":
    text_to_speak = """
    Verse 1
It's late in the evening; glass on the side
I've been sat with you for most of the night
Ignoring everybody here
We wish they would disappear
So maybe we could get down now

Chorus
I need you, darling
Come on, set the tone
If you feel like letting me know
Come on, and let me know
Do you want me to come on over?
I need you, darling
Come on, set the tone
If you love me
Come on, get involved

Verse 2
Oh, let's fall in love again
Sing!
Kiss me under the milky twilight
Lead me out on the moonlit floor
Lift your open hand
Strike up the band, and make the fireflies dance
Silver moon's sparkling
So kiss me under the milky twilight
Let's fall in love again

Chorus
I need you, darling
Come on, set the tone
If you feel like letting me know
Come on, and let me know
Do you want me to come on over?
I need you, darling
Come on, set the tone
If you love me
Come on, get involved

Bridge
(Can you feel it?) All the guys in here don't even wanna dance
Just bring it in closer, oh, closer
(Can you feel it?) Don't you know baby girl, that this is love?
And this music's for makin' love

Chorus
I need you, darling
Come on, set the tone
If you love me
Come on, get involved

Interlude
(Sing!) I need you, darling
(Sing!) If you love me

Outro
Woah-oh (can you feel it?)
Before the beat kicks in again? Can you feel it? Can you feel it?
Woah-oh
Woah-oh-oh, no, no, no, ow!
Won't you let me know?
Won't you let me know?
Can you feel it?
Can you feel it?
Can you feel it?
Before the beat kicks in again? Can you feel it? Can you feel it?
Won't you let me know?
    """
    output_file = "sing.wav"
    generate_and_save_voice(text_to_speak, output_file)
    print(f"Voice generated and saved as '{output_file}'")
