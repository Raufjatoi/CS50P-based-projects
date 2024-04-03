import pyttsx3

def generate_and_save_voice(text, output_file):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Find the voice that sounds closest to Ed Sheeran
    ed_sheeran_voice = None
    for voice in engine.getProperty('voices'):
        if "Ed Sheeran" in voice.name:
            ed_sheeran_voice = voice
            break
    
    # Set the selected voice
    if ed_sheeran_voice:
        engine.setProperty('voice', ed_sheeran_voice.id)
    else:
        print("Ed Sheeran voice not found. Using default voice.")

    # Set medium speed
    engine.setProperty('rate', 150)  # Adjust as needed

    # Generate the voice for the given text
    engine.save_to_file(text, output_file)

    # Run the engine
    engine.runAndWait()

if __name__ == "__main__":
    text_to_speak = """
    Hello there, I'm Rauf, here's a song,
    Let me take you on a journey, it won't be long.
    About a lad named JB, with dreams to chase,
    In the melody of life, he found his place.

    Born in a town where the stars rarely gleamed,
    JB's eyes held visions far beyond what seemed.
    With a guitar in hand and a heart full of dreams,
    He strummed his way through life's intricate schemes.

    From the streets of Stratford, where he first sang,
    To the world's grand stages, where his voice rang.
    Each chord he played, each note he sang,
    Was a tale of his journey, where hopes sprang.

    Through the bustling crowds and the silent nights,
    JB's music soared to unimaginable heights.
    With every verse, he wrote his story,
    A tale of resilience, guts, and glory.

    From humble beginnings, he made his stand,
    A beacon of hope in a faraway land.
    Through fame's blinding lights and fortune's call,
    He remained true, never afraid to fall.

    In the quiet moments, amidst the fame,
    JB found solace in his own refrain.
    A melody of memories, a symphony of dreams,
    His music carried echoes of timeless themes.

    As the years passed by, JB's legacy grew,
    His songs touching hearts, both old and new.
    With every strum, with every chord,
    He inspired souls, struck a universal chord.

    So here's to JB, in the hall of fame,
    Where his music echoes, forever the same.
    A troubadour of life, a bard of the heart,
    His melodies linger, never to depart.
    """
    output_file = "cool_melody_voice.wav"
    generate_and_save_voice(text_to_speak, output_file)
    print(f"Voice generated and saved as '{output_file}'")
