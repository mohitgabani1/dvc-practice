from pathlib import Path
import pickle


def save_object(file_path: str | Path, obj: object) -> None:
    """Save a Python object to a file."""

    file_path = Path(file_path)

    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(file_path, "wb") as file:
            pickle.dump(obj, file)
    except Exception as exc:
        raise RuntimeError(
            f"Failed to save object to {file_path}"
        )
