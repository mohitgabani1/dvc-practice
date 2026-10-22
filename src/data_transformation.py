from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler

from src.object_utils import save_object

train_data_path = Path("data/validation/train.csv")


def transformation():
    train_data = pd.read_csv(train_data_path)
    x_train = train_data.drop(columns=["Outcome"])

    ct = ColumnTransformer(
        transformers=[
            (
                "scaler",
                StandardScaler(),
                [
                    "Pregnancies",
                    "Glucose",
                    "BloodPressure",
                    "SkinThickness",
                    "Insulin",
                    "BMI",
                    "DiabetesPedigreeFunction",
                    "Age",
                ],
            )
        ]
    )
    ct.fit_transform(x_train)
    artifact_path = Path("data/artifacts/preprocessed.pkl")
    artifact_path.parent.mkdir(parents=True, exist_ok=True)
    save_object(artifact_path, obj=ct)


if __name__ == "__main__":
    transformation()
