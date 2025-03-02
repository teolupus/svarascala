"""
Setup script for SvaraScala.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="svarascala",
    version="0.1.0",
    author="Bruno Lago",
    author_email="teolupus@gmail.com",
    description="A library for calculating musical frequencies across Western and Indian musical systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/teolupus/svarascala",
    project_urls={
        "Bug Tracker": "https://github.com/teolupus/svarascala/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    packages=find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "svarascala=svarascala.__main__:main",
        ],
    },
)