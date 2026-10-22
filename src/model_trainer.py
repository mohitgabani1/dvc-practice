from pathlib import Path

import pandas as pd
import yaml
from sklearn.ensemble import RandomForestClassifier

from src.object_utils import load_object, save_object

train_data_path = Path("data/validation/train.csv")
preprocessed_path = Path("data/artifacts/preprocessed.pkl")
model_path = Path("data/artifacts/model.pkl")
model_path.parent.mkdir(parents=True, exist_ok=True)


def trainer():
    train_data = pd.read_csv(train_data_path)
    x_train = train_data.drop(columns=["Outcome"])
    y_train = train_data["Outcome"]
    with open("params.yaml", "r") as f:
        params = yaml.safe_load(f)
    ct = load_object(preprocessed_path)
    rf = RandomForestClassifier(
        n_estimators=params["model parameter"]["n_estimators"],
        criterion=params["model parameter"]["criterion"],
        max_depth=params["model parameter"]["max_depth"],
        ccp_alpha=params["model parameter"]["ccp_alpha"],
    )

    x_train_transformed = ct.transform(x_train)
    rf.fit(x_train_transformed, y_train)
    save_object(model_path, rf)


if __name__ == "__main__":
    trainer()
