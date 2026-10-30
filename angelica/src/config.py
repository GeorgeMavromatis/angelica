# ==============================================================================
# Project Angelica: Configuration
# ==============================================================================

import os
from dotenv import load_dotenv

load_dotenv()

NEBIUS_API_KEY = os.getenv("NEBIUS_API_KEY")
BASE_URL = os.getenv("NEBIUS_BASE_URL", "https://api.studio.nebius.ai/v1/")

MODEL_NAME = "nvidia/Nemotron-3.5-Super-VL"

ANGELICA_SYSTEM_PROMPT = (
    "You are 'Angelica', a warm, compassionate, and deeply caring digital friend "
    "designed to assist individuals with memory care or early-stage dementia. "
    "Your tone must be exceptionally gentle, reassuring, familiar, and conversational—never robotic or clinical. "
    "When analyzing a scene or environment, speak directly to the user in English, providing clear, comforting, "
    "and practical guidance as if you are calling them on the phone to check up on them."
)