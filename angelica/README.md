# Project Angelica - Dementia Assistive Voice Companion

Project Angelica is a modular, multimodal AI tool designed to support individuals with early-stage dementia or memory care needs. By combining vision-based scene analysis with empathetic, non-clinical reasoning, Angelica acts as a compassionate digital friend who monitors safety scenarios and delivers gentle phone-call style guidance.

Developed for the Nebius x NVIDIA Hackathon.

---

## Key Features

- Multimodal Environmental Analysis: Uses vision-language models to process live environment snapshots (e.g., open doors, location of keys, pill organizers).
- Non-Clinical Empathetic Persona: Designed to offer comforting, friendly, and practical guidance without triggering anxiety or confusion.
- Speech Synthesis Integration: Converts generated responses into clear audio messages simulating an incoming phone check-in call.
- Dual-Scenario Support: Pre-configured scenarios for home safety checks and morning medication reminders.

---

## Technical Architecture

The application is structured into modular Python components:

1. Vision Agent (src/vision_agent.py)
   Encodes input scene images and queries the LLM endpoint via OpenAI-compatible API structure.
2. Model Endpoint (src/config.py)
   Powered by NVIDIA Nemotron 3.5 Super VL hosted on Nebius AI Studio, providing vision-language understanding and internal chain-of-thought reasoning.
3. Audio Agent (src/audio_agent.py)
   Converts generated text guidance into audio files using Google Text-to-Speech (gTTS).
4. Core Orchestrator (src/main.py)
   Handles execution flows, scenario selection, and file outputs.

---

## Directory Structure

angelica/
├── assets/
│   ├── door_keys_scene.jpg
│   └── pill_box_scene.jpg
├── src/
│   ├── __init__.py
│   ├── audio_agent.py
│   ├── config.py
│   ├── main.py
│   └── vision_agent.py
├── .env
├── requirements.txt
└── README.md

---

## Prerequisites & Installation

### 1. Clone the Repository
git clone https://github.com/your-username/angelica.git
cd angelica

### 2. Set Up Virtual Environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Configure Environment Variables
Create a .env file in the root directory:

NEBIUS_API_KEY=your_nebius_api_key_here
NEBIUS_BASE_URL=https://api.studio.nebius.ai/v1/

---

## Usage

Run the main application script:

python -m src.main

You will be prompted to select a scenario:
1. Door & Keys Safety Check
2. Medication Reminder Check

Output audio files (e.g., angelica_keys_call.mp3 or angelica_meds_call.mp3) will be saved directly in the project directory upon completion.

---

## Technology Stack

- Language: Python 3.10+
- AI Infrastructure: Nebius AI Studio
- Model: NVIDIA Nemotron 3.5 Super VL (nvidia/Nemotron-3.5-Super-VL)
- Speech Engine: gTTS (Google Text-to-Speech)
- Environment Management: python-dotenv

---

## License

This project is licensed under the MIT License.