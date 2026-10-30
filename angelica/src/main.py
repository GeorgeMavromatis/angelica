# ==============================================================================
# Project Angelica: Main Entry Point
# Description: Connects Vision Agent with Audio Agent to execute multiple scenarios.
# ==============================================================================

import os
from src.vision_agent import VisionAgent
from src.audio_agent import AudioAgent

SCENARIOS = {
    "1": {
        "name": "Door & Keys Safety Check",
        "image": os.path.join("assets", "door_keys_scene.jpg"),
        "output_audio": "angelica_keys_call.mp3",
        "query": (
            "Analyze the scene. The front door is open and the keys are missing from the table. "
            "Generate a warm, spoken phone call message as a caring friend reminding them where their keys are, "
            "or gently guiding them back."
        )
    },
    "2": {
        "name": "Medication Reminder Check",
        "image": os.path.join("assets", "pill_box_scene.jpg"),
        "output_audio": "angelica_meds_call.mp3",
        "query": (
            "Analyze the scene. Look at the pill organizer and water glass on the table. "
            "Determine if the morning medication is still inside. Generate a gentle, reassuring "
            "phone call message reminding them to take their morning pills with water."
        )
    }
}

def run_scenario(scenario_key: str):
    scenario = SCENARIOS[scenario_key]
    print(f"\n==================================================")
    print(f" Running Scenario [{scenario_key}]: {scenario['name']}")
    print(f"==================================================")

    image_path = scenario["image"]

    if not os.path.exists(image_path):
        print(f"\n[WARNING] Image not found at path: {image_path}")
        print(f"Please place an image at '{image_path}' to run this scenario.")
        return

    print(f"\n[1/3] Loading and analyzing image from: {image_path}...")
    
    vision_agent = VisionAgent()
    response_text = vision_agent.analyze_scene(image_path, custom_query=scenario["query"])
    
    print(f"\n[AI Response Generated]:\n\"{response_text}\"")

    print(f"\n[2/3] Developing voice message...")
    audio_agent = AudioAgent(output_filename=scenario["output_audio"])
    audio_file = audio_agent.synthesize_and_simulate_call(response_text)

    if audio_file:
        print(f"\n[3/3] Process completed successfully!")
        print(f"👉 Audio saved to '{audio_file}'.")
    else:
        print("\n[ERROR] Something went wrong with the mp3 file.")

def main():
    print("==================================================")
    print("   Starting Project Angelica MVP (Dementia Assist) ")
    print("==================================================")
    print("Select a scenario to run:")
    print("1. Door & Keys Safety Check")
    print("2. Medication Reminder Check")
    
    choice = input("\nEnter choice (1 or 2) [default: 1]: ").strip()
    if choice not in SCENARIOS:
        choice = "1"
        
    run_scenario(choice)

if __name__ == "__main__":
    main()