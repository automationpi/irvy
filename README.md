# Irvy

Irvy is a command-line tool to setup projects for Selenium and Playwright in different languages.

In an ever-evolving technological landscape, the demand for efficient and versatile test automation tools has never been greater. Irvy, a command-line interface tool, steps up to this challenge by streamlining the setup process for test automation across a broad spectrum of programming languages. Whether you are a novice entering the world of automation engineering or a seasoned veteran, Irvy’s ability to provide comparable building blocks facilitates an effortless transition between different programming languages such as Java, C#, or JavaScript.

Harnessing the capabilities of popular automation tools like Selenium and Playwright, Irvy empowers users to initiate projects in their language of choice with a simple, interactive command-line interface. This process alleviates the potential complexities associated with the setup phase, allowing users to focus their attention on the development of high-quality, robust automation scripts.

In addition, Irvy fosters an environment of continuous learning and skill diversification. For seasoned professionals who have primarily worked in a single programming language, Irvy offers a comfortable, straightforward entry point to explore and adopt different languages. This not only widens their skillset but also broadens their perspective on the different strategies and approaches to test automation.

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
```
project_name/
|-- .gitignore
|-- README.md
|-- package.json OR requirements.txt OR .csproj
|-- src/
    |-- tests/
        |-- test_example.js OR test_example.py OR test_example.cs
|-- node_modules/ OR venv/ OR packages/
```
# Technologies and Frameworks
Depending on the language and tool you choose, Irvy will use different testing frameworks:

Python: Irvy will use Pytest for both Selenium and Playwright projects.
C#: Irvy will use xUnit for both Selenium and Playwright projects.
JavaScript: Irvy will use Jest for both Selenium and Playwright projects.


# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

irvy.org

# License
MIT