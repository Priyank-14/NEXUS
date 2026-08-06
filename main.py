from core.speech_listener import SpeechListener
from core.command_processor import CommandProcessor

listener = SpeechListener()
processor = CommandProcessor()

command = listener.listen()

print(f"Raw Command: {command}")

action = processor.process(command)

print(f"Processed Action: {action}")