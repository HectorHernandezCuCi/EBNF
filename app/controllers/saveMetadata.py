import json
from pathlib import Path

def saveMetadata(metadata, folder="assets/img"):
    metadataFile = Path(folder) / "metadata.json"
    Path(folder).mkdir(parents=True, exist_ok=True)
    with open(metadataFile, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=4, ensure_ascii=False)