from core.speech_listener import SpeechListener

listener = SpeechListener()

command = listener.listen()

print(f"Returned Command: {command}")