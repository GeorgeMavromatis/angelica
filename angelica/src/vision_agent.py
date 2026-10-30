# ==============================================================================
# Project Angelica: Vision Agent
# Description: Handles image encoding and communication with the Nebius LLM endpoint.
# ==============================================================================

import os
import base64
from openai import OpenAI
from src.config import NEBIUS_API_KEY, BASE_URL, MODEL_NAME, ANGELICA_SYSTEM_PROMPT

class VisionAgent:
    def __init__(self):
        # Initialize OpenAI-compatible client for Nebius AI Studio
        self.client = OpenAI(
            base_url=BASE_URL,
            api_key=NEBIUS_API_KEY
        )

    def _encode_image(self, image_path: str) -> str:
        """Encodes an image file to a base64 string."""
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def analyze_scene(self, image_path: str, custom_query: str = None) -> str:
        """
        Sends the image to the Nebius LLM and returns Angelica's guidance response.
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image not found at path: {image_path}")

        base64_image = self._encode_image(image_path)

        if not custom_query:
            custom_query = (
                "Analyze the scene. The front door is open and the keys are missing from the table. "
                "Generate a warm, spoken phone call message as a caring friend reminding them where their keys are, "
                "or gently guiding them back."
            )

        try:
            response = self.client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": ANGELICA_SYSTEM_PROMPT},
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": custom_query},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{base64_image}"
                                }
                            }
                        ]
                    }
                ],
                max_tokens=2500,  # <-- Αυξήσαμε τα tokens από  σ
                temperature=0.3
            )
            # Print full API response for debugging
            # print(f"\n[DEBUG API RESPONSE]: {response}")

            if response.choices and response.choices[0].message:
                return response.choices[0].message.content
            return "No response received from model."

        except Exception as e:
            print(f"[ERROR] Communication error with Nebius API: {e}")
            return "George, there was a small technical problem, but do not be scared I am still here with you ."