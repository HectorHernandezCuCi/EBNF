from pathlib import Path
from app.controllers.loadMetadata import loadMetadata

def getImageFromFolder(folder="assets/img"):
    metadata = loadMetadata(folder)
    folderPath = Path(folder)
    images = []

    if not folderPath.exists():
        return images

    for file in folderPath.iterdir():
        if file.suffix.lower() in [".png", ".jpg", ".jpeg", ".gif"]:
            fileMeta = metadata.get(file.name, {})
            images.append({
                "path": str(file),
                "name": fileMeta.get("name", file.stem),
                "description": fileMeta.get("description", "")
            })

    return images
