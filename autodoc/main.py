import argparse
import sys
import os
from pathlib import Path
from autodoc.generateDoc import generateDocumentation

def get_api_key():
    # First check environment variable
    api_key = os.environ.get("GEMINI_API_KEY")
    
    # If not in environment, check config file
    if not api_key:
        config_path = Path.home() / ".autodoc" / "config"
        if config_path.exists():
            with open(config_path, "r") as f:
                for line in f:
                    if line.startswith("GEMINI_API_KEY="):
                        api_key = line.split("=")[1].strip()
    
    return api_key

def get_files_content(directory="."):
    """Get content of relevant files in the project."""
    ignored_dirs = {".git", "node_modules", "venv", "env", "build", "dist", "__pycache__","android","build","macos","ios","linux","web","test","windows"}
    ignored_extensions = {".pyc", ".pyo", ".pyd", ".so", ".dll", ".class", ".exe", ".obj", ".o",".h5",".csv"}
    
    all_content = ""
    
    for root, dirs, files in os.walk(directory):
        # Skip ignored directories
        dirs[:] = [d for d in dirs if d not in ignored_dirs]
        
        for file in files:
            if not any(file.endswith(ext) for ext in ignored_extensions):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        all_content += f"\n\nFile: {file_path}\n```\n{content}\n```\n"
                except:
                    # Skip files that can't be read as text
                    pass
    
    return all_content

def write_to_file(content, output_path):
    with open(output_path, "w") as f:
        f.write(content)
    print(f"Documentation written to {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Automatically generate documentation")
    
    # Mutually exclusive group for verbose options
    verbose_group = parser.add_mutually_exclusive_group()
    verbose_group.add_argument("-v", "--verbose", action="store_true", help="Generate verbose README with all details")
    
    # Optional text arguments
    parser.add_argument('--guidance', type=str, nargs='+', 
                        help="Additional guidance for documentation generation")
    
    # Optional output file argument
    parser.add_argument("output", nargs="?", default="README.md", 
                        help="Output file path (default: README.md)")
    
    args = parser.parse_args()
    
    verbose_prompt = """You are an expert project maintainer, you have been assigned this project to document.
You will use shields.io badges to indicate the core technologies/frameworks the project uses.
- If this is a backend project, you will list ALL accessible routes, valid methods(ie POST, GET) and the required and optional params, along with a sample curl request
- For a front end project, emphasize the used UI framework(ie Shadcn), list accessible pages and frequently reused components
- For mobile apps, list installed packages, accessible screens and separated logic functions
Return ONLY the text documentation, properly formatted in markdown.
Do not use any code blocks!

Here are the project files:"""

    not_verbose_prompt="""You are an expert project maintainer, you have been assigned this project to document.
You will use shields.io badges to indicate the core technologies/frameworks the project uses.
- If this is a backend project, you will list important accessible routes, valid methods(ie POST, GET) and the required and optional params
- For a front end project, emphasize the used UI framework(ie Shadcn), list accessible pages
- For mobile apps, list installed packages, accessible screens
Return ONLY the text documentation, properly formatted in markdown.
Do not use any code blocks!

Here are the project files:"""

    api_key = get_api_key()
    if not api_key:
        print("Error: Gemini API key not found. Please set the GEMINI_API_KEY environment variable or create a config file at ~/.autodoc/config")
        sys.exit(1)
    
    files_content = get_files_content()
    if args.text:
        print(f"Genrating documentation with provided guidance to{args.output}")
        documentation = generateDocumentation(prompt= not_verbose_prompt, files=files_content, apikey=api_key, extra_prompt= args.text)
    if args.verbose:
        print(f"Generating verbose documentation to {args.output}")
        documentation = generateDocumentation(prompt=verbose_prompt, files=files_content, apikey=api_key)
    else:
        print(f"Generating standard documentation to {args.output}")
        documentation = generateDocumentation(prompt=not_verbose_prompt, files=files_content, apikey=api_key)
    
    write_to_file(documentation, args.output)

if __name__ == "__main__":
    main()
