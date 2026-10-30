# ==============================================================================
# Project Angelica: Audio Agent
# Description: Handles Text-to-Speech conversion in English and simulates
#              the incoming phone call to the user.
# ==============================================================================

import os
from gtts import gTTS

class AudioAgent:
    def __init__(self, output_filename: str = "angelica_call.mp3"):
        self.output_filename = output_filename

    def synthesize_and_simulate_call(self, text_message: str) -> str:
        """
        Converts Angelica's response into an English audio file (.mp3)
        with a slow, reassuring tone simulating a phone call.
        """
        print(f"\n[📞 ANGELICA PHONE CALL INITIATED]...")
        print(f"🔊 Spoken Message: \"{text_message}\"")

        try:
            if not text_message or text_message.strip() == "None":
                print("[ERROR] No valid text provided for speech synthesis.")
                return None

            # Change language to English ('en')
            tts = gTTS(text=text_message, lang='en', slow=True)
            
            tts.save(self.output_filename)
            print(f"[AUDIO SUCCESS] Audio file saved as '{self.output_filename}'.")
            
            return self.output_filename

        except Exception as e:
            print(f"[ERROR] Error during speech synthesis: {e}")
            return None