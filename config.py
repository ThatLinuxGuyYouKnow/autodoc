import os
from pathlib import Path

def configure_api_key():
    api_key = input("Enter your Gemini API key: ").strip()
    if api_key:
        config_dir = Path.home() / ".autodoc"
        os.makedirs(config_dir, exist_ok=True)

        with open(config_dir / "config", "w") as f:
            f.write(f"GEMINI_API_KEY={api_key}\n")

        print(f"API key saved to {config_dir}/config")
    else:
        print("No API key provided.")

if __name__ == "__main__":
    configure_api_key()
