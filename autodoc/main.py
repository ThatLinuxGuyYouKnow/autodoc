import argparse
import sys
from generateDoc import generateDocumentation


def main():
    parser = argparse.ArgumentParser(description="Automatically generate documentation for backend projects")
    parser.add_argument("-v", "--verbose", action="store_true", help="Generate verbose README with all details")
    parser.add_argument("output", nargs="?", default="README.md", help="Output file path (default: README.md)")
    
    args = parser.parse_args()
    verbose_prompt = """ You are an expert project maintainer, you have been assigned this project to document,
    You will use shields.io badges to indicate the core technologies/frameworks the project uses
    - If this is a backend project, you will list ALL accessible routes, valid methods(ie POST, GET) and the required and optional params, along with a sample curl request and 
    - For a front end project, emphasize the used UI framework(ie Shadcn), list accessible pages and frequently reused components
    - For mobile apps, list installed packages, accessible screens and seprated logic functions
    Return ONLY the text documentation, properly formatted in markdown
    Do not use any code blocks! """

    not_verbose_prompt=""" You are an expert project maintainer, you have been assigned this project to document,
    You will use shields.io badges to indicate the core technologies/frameworks the project uses
    - If this is a backend project, you will list important accessible routes, valid methods(ie POST, GET) and the required and optional params 
    - For a front end project, emphasize the used UI framework(ie Shadcn), list accessible pages
    - For mobile apps, list installed packages, accessible screens

    Return ONLY the text documentation, properly formatted in markdown
    Do not use any code blocks!
     """
 # files = somefancywaytogetallfilecontentwhileigonoringbuildsAndUnecessaryFiles()
 # apiKey = someFancyWayToGetUsersApikeyWhenTheySetItUpInSetup.py()
    if args.verbose:
        print(f"Generating verbose documentation to {args.output}")
        generateDocumentation(prompt=verbose_prompt, files="", apikey="")
    else:
        print(f"Generating standard documentation to {args.output}")
        generateDocumentation(prompt=not_verbose_prompt)
    
 

if __name__ == "__main__":
    main()