from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
long_description = ""
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name="rylr",
    packages=["rylr"],
    version="1.0.1",
    license="MIT",
    description="Python library for RYLR LoRa transceivers to simplifies communication with RYLR modules using Python",
    long_description=long_description,
    url="https://github.com/Michael-Jalloh/RYLR",
    long_description_content_type= "text/markdown",
    author="Michael Jalloh",
    author_email="michaeljalloh19@gmail.com",
    install_requires=["pyserial"],
    package_dir={"rylr":"src/rylr"},
    classifiers= [
        "Development Status :: 4 - Beta",      
        "Intended Audience :: Developers",      
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    platforms=["any"],
    keywords=["RYLR","serial","link","communication","RYLR896","RYLR406"],
    project_urls={
        "issues": "https://github.com/Michael-Jalloh/RYLR/issues",
        "source": "https://github.com/Michael-Jalloh/RYLR"
    },
)