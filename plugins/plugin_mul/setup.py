from setuptools import setup, find_packages

setup(
    name="plugin-mul",
    version="1.0.0",
    entry_points={
        "app_plugins": [
            "mul=some_app.application:Operation",
        ]
    },
    packages=find_packages(),
)
