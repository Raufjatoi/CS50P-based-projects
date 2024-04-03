import pyttsx3
engine = pyttsx3.init() 
engine.setProperty('rate', 150)  # Adjust speed
engine.setProperty('volume', 0.8)  # Adjust volume
engine.say("This is a sample text with adjusted voice settings.")
engine.runAndWait()
