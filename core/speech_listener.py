import speech_recognition as sr

class SpeechListener:
    """
    Handles all speech to text operations
    """
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen(self):
        with self.microphone as source:
            print("Adjusting for ambient noise..")
            self.recognizer.adjust_for_ambient_noise(
                source,
                duration = 1
            )  
            print("Listening....")

            audio = self.recognizer.listen(source)
            print("Audio Captured....")

            try:
                text = self.recognizer.recognize_google(audio)
                return text.lower()
            except sr.UnknownValueError:
                print("Could not understand the audio..")
                return ""
            except sr.RequestError:
                print("Speech Recognition service is unavailable")
                return ""
