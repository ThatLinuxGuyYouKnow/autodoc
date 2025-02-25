from setuptools import setup, find_packages, Command
import os
import sys
from pathlib import Path

class ConfigCommand(Command):
    description = "Configure API key for autodoc"
    user_options = []
    
    def initialize_options(self):
        pass
        
    def finalize_options(self):
        pass
        
    def run(self):
        api_key = input("Enter your Gemini API key: ").strip()
        if api_key:
            config_dir = Path.home() / ".autodoc"
            os.makedirs(config_dir, exist_ok=True)
            
            with open(config_dir / "config", "w") as f:
                f.write(f"GEMINI_API_KEY={api_key}\n")
            
            print(f"API key saved to {config_dir}/config")
        else:
            print("No API key provided.")

# Create a post-install script
def _post_install():
    print("\n" + "=" * 60)
    print("To configure autodoc, run: pip install -e . config")
    print("Or configure later with: python -m autodoc.config")
    print("=" * 60 + "\n")

if "install" in sys.argv or "develop" in sys.argv:
    # Add post-install message
    sys.argv.append("--no-user-cfg")  # This is a workaround to ensure our callback runs
    _post_install()

setup(
    name="autodoc",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'autodoc=autodoc.main:main',
        ],
    },
    cmdclass={
        'config': ConfigCommand,
    },
    install_requires=[
        'requests>=2.25.0',
    ],
    author="Alabi Ayobami",
    author_email="arocket04@gmail.com",
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