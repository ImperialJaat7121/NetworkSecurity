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
    "networksecurity/components/data_ingestion.py",
    "networksecurity/components/data_validation.py",
    "networksecurity/components/data_transformation.py",
    "networksecurity/components/model_trainer.py",
    "networksecurity/constants/__init__.py",
    "networksecurity/constants/training_pipeline/__init__.py",
    "networksecurity/entity/__init__.py",
    "networksecurity/entity/config_entity.py",
    "networksecurity/entity/artifact_entity.py",
    "networksecurity/logging/__init__.py",
    "networksecurity/logging/logger.py",
    "networksecurity/exception/__init__.py",
    "networksecurity/exception/exception.py",
    "networksecurity/pipeline/__init__.py",
    "networksecurity/pipeline/batch_prediction.py",
    "networksecurity/pipeline/training_pipeline.py",
    "networksecurity/utils/main_utils/__init__.py",
    "networksecurity/utils/main_utils/utils.py",
    "networksecurity/utils/__init__.py",
    "networksecurity/utils/ml_utils/__init__.py",
    "networksecurity/utils/ml_utils/metric/__init__.py",
    "networksecurity/utils/ml_utils/metric/classification_metric.py",
    "networksecurity/utils/ml_utils/model/__init__.py",
    "networksecurity/utils/ml_utils/model/estimator.py",
    "networksecurity/cloud/__init__.py",
    "notebooks/experiments.ipynb",
    "data_schema/schema.yaml",
    "templates/table.html"
    "Dockerfile",
    "setup.py",
    "main.py",
    "app.py",
    "push_data.py",
    "test_mongodb.py",
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