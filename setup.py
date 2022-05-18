import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pystashlib",
    version="0.2.6",
    description="A python library for manipulating a stash database",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/7dJx1qP/pystashlib",
    author="7dJx1qP",
    author_email="38586902+7dJx1qP@users.noreply.github.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
    packages=["stashlib"],
    include_package_data=True,
    install_requires=["cloudscraper", "pyyaml", "lxml", "python-dateutil"],
)