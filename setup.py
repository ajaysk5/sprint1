from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="calculator-package",
    version="1.0.0",
    description="A Python package for basic arithmetic operations.",
    long_description_content_type="text/markdown",
    url="https://github.com/ajkaysk5/calculator-package",
    author="Ajay Sreekumar Kuzhuvelil",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.6",
)
