# autodoc

[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Gemini API](https://img.shields.io/badge/Gemini-API-brightgreen)](https://generativelanguage.googleapis.com/v1beta)
[![Requests](https://img.shields.io/badge/requests-2.25.0+-orange)](https://pypi.org/project/requests/)

## Overview

`autodoc` is a command-line tool that automatically generates documentation for projects using the Google Gemini API. It analyzes project files and uses the Gemini API to create a Markdown README file.

## Installation

`pip install autodoc`

After installation, configure your Gemini API key using:

`pip install -e . config`

or manually:

`python -m autodoc.config`


## Usage

`autodoc [options] [output]`

**Options:**

- `-v`, `--verbose`: Generates verbose documentation with more details from project files.
- `output`: Specifies the output file path. Defaults to `README.md`.

## Command-line Interface

The `autodoc` command provides the main functionality:

- `autodoc`: Generates a standard README.md file.
- `autodoc -v`: Generates a verbose README.md with more detailed information.
- `autodoc -v OUTPUT.md`: Generates a verbose README in a file named OUTPUT.md.


## Configuration

The Gemini API key is required.  Set it using:

1.  **Environment Variable:** Set the `GEMINI_API_KEY` environment variable.
2.  **Configuration File:** Create `.autodoc/config` in your home directory with `GEMINI_API_KEY=YOUR_API_KEY`.  The `autodoc config` command creates this file for you.


## How It Works

`autodoc` combines file analysis and the Gemini API:

1.  **File Collection:** Collects relevant file content, excluding common directories (`.git`, `node_modules`, etc.) and files (`.pyc`, `.o`, etc.).
2.  **Prompt Generation:** Creates a prompt for the Gemini API based on collected file content and verbosity level.
3.  **API Call:** Sends the prompt and file content to the Gemini API.
4.  **Documentation Generation:** The Gemini API generates Markdown documentation.
5.  **Output:** Writes the generated documentation to the specified output file.


## Example Usage

For a basic Python project, `autodoc` analyzes project files and generates `README.md`. `autodoc -v` provides more detail.


## Contributing

Contributions are welcome!  Submit issues and pull requests on the project's GitHub repository.

## Fun fact, autodoc wrote its own documentation!(but the human had to add this part lol)

