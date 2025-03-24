# autodoc: Automated Documentation Generator

[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/)
[![Requests](https://img.shields.io/badge/requests-2.25.0+-brightgreen.svg)](https://requests.readthedocs.io/en/latest/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-API-orange.svg)](https://developers.google.com/generativelanguage/)


This project uses the Gemini API to automatically generate documentation for various types of projects.  It intelligently determines the project type (backend, frontend, mobile) and formats the documentation accordingly.


## Usage

1. **Installation:**
   ```bash
   pip install -e .
   ```

2. **Configuration:**
   Configure your Gemini API key using the command:
   ```bash
   python -m autodoc.config
   ```
   Alternatively, you can set the `GEMINI_API_KEY` environment variable.

3. **Generating Documentation:**
   ```bash
   autodoc [output_file]
   ```
   This will generate documentation in `README.md` by default.  You can specify a different output file as shown.  For detailed documentation including all file contents add the `-v` flag :
   ```bash
   autodoc -v [output_file]
   ```
   Additional guidance for the documentation can be added with the `--guidance` flag:
   ```bash
   autodoc --guidance "This is a python backend" "The main function is located in main.py" [output_file]
   ```


##  Documentation Structure

The generated documentation will include:

* **Project Overview:** A brief summary of the project's purpose and functionality.
* **Core Technologies:**  Shields.io badges indicating the key technologies and frameworks used.
* **Specifics based on project type:**

    * **Backend Projects:**  Important accessible routes, valid HTTP methods (GET, POST, etc.), required and optional parameters.  Example cURL commands demonstrating usage.
    * **Frontend Projects:** The UI framework used, a list of accessible pages, and frequently reused components.
    * **Mobile Apps:**  Installed packages, accessible screens, and any significant logic functions.

## Example

The generated documentation will be a comprehensive Markdown file suitable for inclusion in a project repository.


