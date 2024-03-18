"""Setup file for the dining-philosophers package deployment"""

from setuptools import setup, find_packages
from dining_philosophers.version import __version__ as version

with open("README.md", "r") as file:
    description = file.read()

setup(
    name = "dining-philosophers",
    version = version,
    packages = find_packages(),
    install_requires = [],
    entry_points = {
        "console_scripts" : [
            "dining-philosophers = dining_philosophers:main",
        ],
    },
    long_description=description,
    long_description_content_type="text/markdown",
)
