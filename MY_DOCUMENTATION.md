# autodoc

[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Gemini API](https://img.shields.io/badge/Gemini-API-brightgreen)](https://generativelanguage.googleapis.com/v1beta)
[![Requests](https://img.shields.io/badge/requests-2.25.0+-orange)](https://pypi.org/project/requests/)



## Overview

`autodoc` is a command-line tool designed to automatically generate documentation for projects using the Google Gemini API.  It analyzes your project files and uses the Gemini API to create a Markdown README file.


## Installation

```
pip install autodoc
```

After installation, configure your Gemini API key by running:

```
pip install -e . config
```

Alternatively, you can manually configure the key anytime using:

```
python -m autodoc.config
```



## Usage

```
autodoc [options] [output]
```

**Options:**

- `-v`, `--verbose`: Generates verbose documentation that includes more details from project files.
- `output`: Specifies the output file path. Defaults to `README.md`.



## Command-line Interface

The main functionality is provided through the `autodoc` command:

*   `autodoc`: Generates a standard README.md file.
*   `autodoc -v`: Generates a verbose README.md with more detailed information extracted from the code.
*   `autodoc -v OUTPUT.md`: Generates a verbose README in a file named OUTPUT.md.




## Configuration

The Gemini API key is required for `autodoc` to function. You can set the key using one of the following methods:

1.  **Environment Variable:** Set the `GEMINI_API_KEY` environment variable.
2.  **Configuration File:** Create a file named `.autodoc/config` in your home directory and add a line in the format `GEMINI_API_KEY=YOUR_API_KEY`.  The `autodoc config` or `pip install -e . config` commands will automatically create this file for you if you enter your API key through the interactive prompt.


## How It Works

`autodoc` works by combining file analysis and Google Gemini's natural language processing capabilities:

1.  **File Collection:** Collects the content of relevant files in the current directory, excluding common directories such as `.git`, `node_modules`, `venv`, etc. and files like `.pyc`, `.o` etc.
2.  **Prompt Generation:** Constructs a prompt for the Gemini API based on the collected file content and the chosen verbosity level. The prompt instructs the API to generate project documentation.
3.  **API Call:** Sends the prompt and file content to the Gemini API for processing.
4.  **Documentation Generation:** The Gemini API generates Markdown documentation based on the prompt and files.
5.  **Output:** Writes the generated documentation to the specified output file.




## Example Usage



Assuming a basic Python project, running `autodoc` would analyze the project's files and generate a `README.md` file.  Using `autodoc -v` would result in a more detailed `README.md`.


## Contributing

Contributions are welcome! Please submit issues and pull requests on the project's GitHub repository.
