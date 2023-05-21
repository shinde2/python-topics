from setuptools import setup, find_packages

setup(
    name="plugin-div",
    version="1.0.0",
    entry_points={
        "app_plugins": [
            "div=application:Operation",
        ]
    },
    packages=find_packages(),
    scripts=["application.py"]
)
