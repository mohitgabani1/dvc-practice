import pandas as pd
from pathlib import Path
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from src.object_utils import save_object

train_data_path = Path("data/validation/train.csv")


def transformation():
    train_data = pd.read_csv(train_data_path)
    x_train = train_data.drop(column=['Outcome'])
    y_train = train_data['Outcome']

    ct = ColumnTransformer(
        transformers=[
            ('scaler', StandardScaler(), ['Pregnancies', 'Glucose', 'BloodPressure',
                                          'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])
        ]
    )
    x_train_transformed = ct.fit_transform(x_train)
    artifact_path = Path("data/artifacts/preprocessed.pkl")
    artifact_path.parent.mkdir(parents=True, exist_ok=True)
    save_object(artifact_path, obj=ct)


if __name__ == '__main__':
    transformation()
