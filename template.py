import os
from pathlib import Path
import logging

project_name = "NetworkSecurity"

list_of_files = [
    ".gitignore",
    ".github/workflows/main.yml",
    # "Network_Data/sample_data.csv",
    "networksecurity/__init__.py",
    "networksecurity/components/__init__.py",
    "networksecurity/constants/__init__.py",
    "networksecurity/entity/__init__.py",
    "networksecurity/logging/__init__.py",
    "networksecurity/exception/__init__.py",
    "networksecurity/pipeline/__init__.py",
    "networksecurity/utils/__init__.py",
    "networksecurity/cloud/__init__.py",
    "notebooks/experiments.ipynb",
    "Dockerfile",
    "setup.py",
    "README.md",
    "requirements.txt",
    ".env",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file : {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")