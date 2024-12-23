from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from app.services.remove_bg import remove_background
import os
import uuid

app = FastAPI()

UPLOAD_FOLDER = "uploads/"
PROCESSED_FOLDER = "processed/"

# Ensure directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    try:
        # Save the uploaded file
        input_file_path = os.path.join(UPLOAD_FOLDER, f"{uuid.uuid4()}.png")
        with open(input_file_path, "wb") as f:
            f.write(await file.read())

        # Process the image
        output_file_path = os.path.join(PROCESSED_FOLDER, f"{uuid.uuid4()}.png")
        remove_background(input_file_path, output_file_path)

        return FileResponse(output_file_path, media_type="image/png", filename="processed-image.png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing image: {e}")
