from setuptools import setup, find_namespace_packages, find_packages

setup(
    name="mul-pkg",
    version="1.0.0",
    packages=find_namespace_packages(include=["math_namespace.*"]),
    #packages=find_packages(include=["math.*"]),
)
