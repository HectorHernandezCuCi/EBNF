import json
from pathlib import Path

def loadMetadata(folder="assets/img"):
    metadataFile = Path(folder) / "metadata.json"
    if not metadataFile.exists():
        return {}  # No file yet, return empty dict

    try:
        with open(metadataFile, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # File is empty or invalid, return empty dict
        return {}
