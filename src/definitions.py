from pathlib import Path


PROJECT_ROOT_DIR = Path(__file__).parent.parent.absolute()

LOGGING_CONFIG_PATH = PROJECT_ROOT_DIR / "logging.ini"

RAW_DATA_FOLDER = PROJECT_ROOT_DIR / "data" / "raw"
PROCESSED_DATA_FOLDER = PROJECT_ROOT_DIR / "data" / "processed"
ECONOMIC_DATASET_FILENAME = "economic_1995_1997.csv"

LOG_PERIOD = 100

MODELS_FOLDER = PROJECT_ROOT_DIR / "models"
