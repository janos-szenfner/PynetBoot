#!/usr/bin/env python3
"""
Setup script for PyNetboot Python rewrite.
"""

import os
import sys
from pathlib import Path
from setuptools import setup, find_packages

# Get version from package
PACKAGE_NAME = "pynetboot"
PACKAGE_DIR = Path(__file__).parent / "src" / PACKAGE_NAME

# Read version from __init__.py
init_path = PACKAGE_DIR / "__init__.py"
version = "0.1.0"
if init_path.exists():
    for line in init_path.read_text().split('\n'):
        if line.startswith('__version__'):
            version = line.split('=')[1].strip().strip("'").strip('"')
            break

# Read requirements
requirements_path = Path(__file__).parent / "requirements.txt"
requirements = []
if requirements_path.exists():
    with open(requirements_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and not line.startswith('-'):
                requirements.append(line)

# Read long description
readme_path = Path(__file__).parent / "README.md"
long_description = ""
if readme_path.exists():
    long_description = readme_path.read_text()


setup(
    name="pynetboot",
    version=version,
    description="A lightweight cross-platform tool for creating bootable USB drives from ISO files (CustomTkinter)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Janos Szenfner",
    author_email="szenfner@outlook.com",
    url="https://github.com/janosszenfner/unetbootin-python",
    license="GPLv2+",

    # Package configuration
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.10",

    # Dependencies
    install_requires=[
        "customtkinter>=6.0.0",
        "Pillow>=13.0.0",
        "requests>=2.34.2",
        "psutil>=7.2.2",
    ],
    extras_require={
        "linux": ["pyudev>=0.24.5"],
        "all": [
            "pyudev>=0.24.5",
            "py7zr>=1.1.4",
            "beautifulsoup4>=4.15.0",
            "pycdlib>=1.22.0",
        ],
        "development": [
            "pytest>=9.2.0",
            "black>=26.10.1",
            "mypy>=2.4.1",
            "pylint>=4.1.3",
            "setuptools>=84.2.1",
        ],
    },

    # Entry points
    entry_points={
        "console_scripts": [
            "pynetboot=pynetboot.main:main",
            "pynetboot-cli=pynetboot.main:main",
        ],
        "gui_scripts": [
            # For macOS app bundle support
        ],
    },

    # Data files — bundled resources the app loads at runtime (bootloader
    # binaries, icons, translation catalogs). Paths match the real layout so
    # they are actually included in wheels/sdists and PyInstaller bundles.
    include_package_data=True,
    package_data={
        "pynetboot": [
            "resources/bootloader/*",
            "resources/bootloader/efi64/*",
            "resources/icons/*",
            "resources/logos/*",
            "resources/translations/*.ts",
        ],
    },

    # Classifiers
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: System :: Installation/Setup",
        "Topic :: System :: Boot :: Init",
        "Topic :: Utilities",
    ],
)
