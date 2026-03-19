from fastapi import FastAPI, UploadFile, File
import shutil

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    file_location = f"temp_{file.filename}"

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 🔴 LOAD YOUR MODEL HERE
    # prediction = your_model_predict(file_location)

    prediction = "Cancer: Negative"  # replace with real output

    return {"result": prediction}
