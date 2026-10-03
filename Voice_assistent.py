import pyttsx3
import speech_recognition as sr
import time

def setup_alexa_female_voice(engine):
    """Configures voice properties for a natural, human-like female English accent."""
    voices = engine.getProperty('voices')
    selected_voice_id = None
    
    
    for voice in voices:
        voice_name = voice.name.lower()
        if 'zira' in voice_name or 'samantha' in voice_name or 'victoria' in voice_name or 'female' in voice_name:
            selected_voice_id = voice.id
            break
            
    
    if not selected_voice_id and len(voices) > 1:
        selected_voice_id = voices[1].id
    elif not selected_voice_id and len(voices) > 0:
        selected_voice_id = voices[0].id

    if selected_voice_id:
        engine.setProperty('voice', selected_voice_id)

    
    engine.setProperty('rate', 135) 
    engine.setProperty('volume', 1.0) 

def speak(text):
    """Speaks the exact input text as-is using the fine-tuned female voice."""
    print(f"🔊 [ASSISTANT]: \"{text}\"")
    
    engine = pyttsx3.init()
    setup_alexa_female_voice(engine)
    
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def main():
    recognizer = sr.Recognizer()

    print("=" * 60)
    print("         ALEXA-STYLE CONTINUOUS VOICE ECHO SYSTEM          ")
    print("=" * 60)
    print("  • Listening continuously with no time limits.")
    print("  • Speak freely; output starts when you complete a sentence.")
    print("  • Press Ctrl+C in terminal to stop.")
    print("=" * 60 + "\n")

    try:
        with sr.Microphone() as source:
            print("⚙️ [CALIBRATING] Adjusting for room background noise (1 sec)...")
            recognizer.adjust_for_ambient_noise(source, duration=1.0)
            print("✅ [READY] Mic calibrated! Start talking whenever you're ready.\n")

            while True:
                try:
                    print("-" * 50)
                    print("🎙️ [LISTENING...] Speak your sentence now...")
                    
                    
                    audio = recognizer.listen(source, timeout=None, phrase_time_limit=None)
                    
                    print("⚙️ [PROCESSING] Converting speech to text...")
                    
                    
                    recognized_text = recognizer.recognize_google(audio)
                    print(f"💬 [USER]: \"{recognized_text}\"")

                    if recognized_text.lower() in ["exit", "quit", "stop program", "bye alexa"]:
                        print("\n🛑 Exit command detected.")
                        speak("Goodbye!")
                        break

                    
                    speak(recognized_text)

                except sr.UnknownValueError:
                    
                    print("⚠️ [UNRECOGNIZED] Noise detected, but no clear speech. Listening again...")

                except sr.RequestError as e:
                    print(f"❌ [NETWORK ERROR] Speech service connection failed: {e}")
                    time.sleep(2)

    except KeyboardInterrupt:
        print("\n\n🛑 Assistant stopped manually by user (Ctrl+C). Goodbye!")
    except Exception as e:
        print(f"\n❌ System Error: {e}")

if __name__ == "__main__":
    main()





