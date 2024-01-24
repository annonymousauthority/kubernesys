from fastapi import APIRouter
from fastapi import FastAPI, File, UploadFile, HTTPException
import os

router = APIRouter()


@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    try:
        upload_folder = "file_storage"
        os.makedirs(upload_folder, exist_ok=True)

        # Construct the full file path
        file_path = os.path.join(upload_folder, file.filename)

        with open(file_path, "wb") as f:
            f.write(file.file.read())
        return {"filename": file.filename}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
