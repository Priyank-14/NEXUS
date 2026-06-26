import pyttsx3
class VoiceEngine:
    """
    Handles all text-to-speech operations for Nexus.
    """

    def __init__(self):
        self.engine = pyttsx3.init()

    def speak(self, text: str):
        """
        Converts text into speech.

        Args:
            text (str): The sentence to be spoken.
        """
        self.engine.say(text)
        self.engine.runAndWait()