from setuptools import setup, find_packages

setup(
    name="app-pkg",
    version="1.0.0",
    entry_points={
        "console_scripts": [
            "run-app=example:run_app",
        ]
    },
    packages=find_packages(),
    scripts=["example.py"]
)
