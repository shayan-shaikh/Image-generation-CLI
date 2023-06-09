from os.path import abspath, dirname, join, isfile
from os import environ
from setuptools import find_packages, setup
import sys

this_dir = abspath(dirname(__file__))
with open(join(this_dir, "README.md"), encoding="utf-8") as file:
    long_description = file.read()


setup(
    name="imggencli",
    python_requires=">3.5",
    options={"bdist_wheel": {"universal": "1"}},
    version="1.4.4",
    description="A command line application to generate customized images based on the Open AI API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shayan-shaikh/Image-generation-CLI",
    author="Shayan Shaikh",
    license="Open Source",
    author_email="Shaikhshayan1@gmail.com",
    keywords=["cli", "developer tools", "productivity", "openai", "generative art", "ai"],
    packages=find_packages(),
    install_requires=["click==8.1.3", "openai==0.27.2", "rich==13.3.1", "idna", "pillow"],
    entry_points={"console_scripts": ["imggencli=imggencli.cli:cli"]},

)
