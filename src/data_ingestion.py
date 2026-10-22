from pathlib import Path

import pandas as pd


def ingestion():
    df = pd.read_csv(
        "/Volumes/Learning/Projects/ML Projects/Classification/Diabetes/diabetes_v1.csv")

    raw_data_path = Path("data/raw/data.csv")
    raw_data_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(raw_data_path, index=False)


if __name__ == '__main__':
    ingestion()
