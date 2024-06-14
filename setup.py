from setuptools import setup, find_packages
# read the contents of your README file
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(
    path.join(this_directory, "README.md"), encoding="utf-8"
) as f:
    long_description = f.read()

required = [
    "openai",
    "pandas",
    "streamlit",
    "python-dotenv",
    "PyYAML"
]

setup(
    name="chatgpt-emailapp",
    version="0.1",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=required,
)