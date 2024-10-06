from fastapi import FastAPI, UploadFile, HTTPException
from PIL import Image, UnidentifiedImageError
import pytesseract as ocr
import pathlib
import io

from models.DrugInfo import DrugInfo
from services.LoggerService import Logger


BASE_DIR = pathlib.Path(__file__).parent
UPLOAD_DIR = BASE_DIR / "uploads"

logger = Logger.getLogger(__name__)
app = FastAPI()

@app.get("/health")
def health():
    return {"ping": "pong"}

@app.post("/druglabel")
async def druglabel(file: UploadFile):
    logger.info('this is a debug message')
    bytes = io.BytesIO(await file.read())

    try:
        img = Image.open(bytes)
    except UnidentifiedImageError: 
        raise HTTPException(detail="Invalid image", status_code=400)
    
    resultF = ocr.image_to_string(img, lang="tha+eng")
    result = DrugInfo.fromString(resultF)

    return {
        "filename": file.filename,
        "info": result
    }
    