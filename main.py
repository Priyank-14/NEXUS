from core.voice_engine import VoiceEngine


def main():
    print("Initializing Nexus...")

    voice = VoiceEngine()

    voice.speak("Hello Priyank. I am Nexus.")


if __name__ == "__main__":
    main()