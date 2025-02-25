from setuptools import setup, find_packages
import os
import sys
from pathlib import Path

def prompt_for_api_key():
    api_key = input("Enter your Gemini API key (press Enter to skip and configure later): ").strip()
    if api_key:
        # Create config directory if it doesn't exist
        config_dir = Path.home() / ".autodoc"
        os.makedirs(config_dir, exist_ok=True)
        
        # Write API key to config file
        with open(config_dir / "config", "w") as f:
            f.write(f"GEMINI_API_KEY={api_key}\n")
        
        print(f"API key saved to {config_dir}/config")
    else:
        print("\nYou can set your API key later by:")
        print("1. Setting the GEMINI_API_KEY environment variable, or")
        print("2. Creating a file at ~/.autodoc/config with content: GEMINI_API_KEY=your_key_here")

# Only prompt during install command
if "install" in sys.argv:
    prompt_for_api_key()

setup(
    name="autodoc",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'autodoc=autodoc.main:main',
        ],
    },
    install_requires=[
        'requests>=2.25.0',
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool to automatically generate documentation for projects using Gemini API",
    keywords="documentation, generator, gemini, api",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)