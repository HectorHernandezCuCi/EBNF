from tkinter import filedialog, simpledialog
import shutil
from pathlib import Path
from app.controllers.loadMetadata import loadMetadata
from app.controllers.saveMetadata import saveMetadata


def addFile(imagesList, updateCallback, saveFolder="assets/img"):
    filePath = filedialog.askopenfilename(
        title="Selecciona diagramas",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif")]
    )

    if filePath:
        saveFolderPath = Path(saveFolder)
        saveFolderPath.mkdir(parents=True, exist_ok=True)
        destinationPath = saveFolderPath / Path(filePath).name
        shutil.copy(filePath, destinationPath)

        # Ask for custom name and description
        imageName = simpledialog.askstring(
            "Nombre de la imagen",
            "Ingresa el nombre de la imagen:",
            initialvalue=Path(filePath).stem
        )
        imageDesc = simpledialog.askstring(
            "Descripción",
            "Ingresa la descripción de la imagen:",
            initialvalue=""
        )

        # Add to images list
        imgData = {
            "path": str(destinationPath),
            "name": imageName or Path(filePath).stem,
            "description": imageDesc or ""
        }
        imagesList.append(imgData)

        # Load existing metadata, update it, and save
        metadata = loadMetadata(saveFolder)
        metadata[destinationPath.name] = {
            "name": imgData["name"],
            "description": imgData["description"]
        }
        saveMetadata(metadata, saveFolder)

        updateCallback()
