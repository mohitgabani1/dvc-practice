from pathlib import Path
from sklearn.model_selection import train_test_split
import pandas as pd

data_path = Path("data/raw/data.csv")
train_data_path = Path("data/validation/train.csv")
test_data_path = Path("data/validation/test.csv")


def validation():
    df = pd.read_csv(data_path)
    train, test = train_test_split(df, random_state=42, test_size=0.2)
    train_data_path.parent.mkdir(parents=True, exist_ok=True)
    test_data_path.parent.mkdir(parents=True, exist_ok=True)

    train.to_csv(train_data_path, index=False)
    test.to_csv(test_data_path, index=False)


if __name__ == '__main__':
    validation()
