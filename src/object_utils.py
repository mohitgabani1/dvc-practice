import pickle
from pathlib import Path


def save_object(file_path: str | Path, obj: object) -> None:
    """Save a Python object to a file."""

    file_path = Path(file_path)

    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(file_path, "wb") as file:
            pickle.dump(obj, file)
    except (OSError, pickle.PickleError, TypeError, AttributeError) as exc:
        raise RuntimeError(f"Failed to save object to {file_path}") from exc


def load_object(file_path: str | Path):
    """Load a Python object from a file."""

    file_path = Path(file_path)

    try:
        with open(file_path, "rb") as file:
            return pickle.load(file)

    except (OSError, pickle.PickleError, TypeError, AttributeError) as exc:
        raise RuntimeError(
            f"Failed to save object to {file_path}") from exc
