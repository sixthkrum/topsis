import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="TOPSIS-Vikram-101803368",
    version="1.0.1",
    description="Apply topsis to a dataset in a csv file",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/sixthkrum/topsis",
    author="Vikram Alagh",
    author_email="valagh_be18@thapar.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["topsis"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "csvTopsis=topsis.__main__:main",
        ]
    },
)
