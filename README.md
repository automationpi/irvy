# Irvy

Irvy is a command-line tool to setup projects for Selenium and Playwright in different languages.

## Features
- Setup Selenium projects in Python, C#, and JavaScript.
- Setup Playwright projects in Python, C#, and JavaScript.
- Interactive command-line interface.

## Installation
You can install Irvy using pip:
```bash
pip install irvy
```

# Usage
You can run Irvy with the following command:
```bash
irvy
```
This will start an interactive command-line interface where you can choose the language and tool you want to use for your project.

![image](https://github.com/automationpi/irvy/assets/82222256/2b680165-c947-4bfb-ae3c-cac93a012294)
Select technology

![image](https://github.com/automationpi/irvy/assets/82222256/85b840fa-4232-4f99-bee8-df8a90495c46)
Select tool you want to use

# Project Structure
project_name/
|-- .gitignore
|-- README.md
|-- package.json OR requirements.txt OR .csproj
|-- src/
    |-- tests/
        |-- test_example.js OR test_example.py OR test_example.cs
|-- node_modules/ OR venv/ OR packages/

# Technologies and Frameworks
Depending on the language and tool you choose, Irvy will use different testing frameworks:

Python: Irvy will use Pytest for both Selenium and Playwright projects.
C#: Irvy will use xUnit for both Selenium and Playwright projects.
JavaScript: Irvy will use Jest for both Selenium and Playwright projects.


# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

# License
MIT
