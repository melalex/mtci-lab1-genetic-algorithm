import logging
import logging.config

import pandas as pd
from src.definitions import (
    ECONOMIC_DATASET_FILENAME,
    LOGGING_CONFIG_PATH,
    PROCESSED_DATA_FOLDER,
    RAW_DATA_FOLDER,
)


def process_raw_dataset(logger: logging.Logger):
    target_path = PROCESSED_DATA_FOLDER / ECONOMIC_DATASET_FILENAME
    if target_path.exists():
        logger.info("File [ %s ] exist. Skipping dataset processing...", target_path)
    else:
        dataset = pd.read_csv(
            RAW_DATA_FOLDER / ECONOMIC_DATASET_FILENAME, sep="\t"
        ).rename(
            columns={
                "M0": "M0(-7)",
                "M2": "M2(-7)",
                "IOC": "IOC(0)",
                "IPC": "IPC(0)",
                "KVVE": "KVVE(-7)",
            }
        )

        dataset["IPC(+1)"] = dataset["IPC(0)"]

        dataset["M0(-7)"] = dataset["M0(-7)"].shift(periods=7)
        dataset["M2(-7)"] = dataset["M2(-7)"].shift(periods=7)
        dataset["KVVE(-7)"] = dataset["KVVE(-7)"].shift(periods=7)
        dataset["IPC(+1)"] = dataset["IPC(+1)"].shift(periods=-1)

        PROCESSED_DATA_FOLDER.mkdir()

        dataset.dropna().to_csv(target_path, index=False)

        logger.info("Saved processed dataset to [ %s ]", target_path)


if __name__ == "__main__":
    logging.config.fileConfig(LOGGING_CONFIG_PATH)
    process_raw_dataset(logging.getLogger(__name__))
