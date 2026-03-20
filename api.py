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

import tensorflow as tf
from PIL import Image
import numpy as np

model = tf.keras.models.load_model("model.h5")

def predict_image(path):
    img = Image.open(path).resize((224, 224))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    pred = model.predict(img)[0][0]

    return "Cancer: Positive" if pred > 0.5 else "Cancer: Negative"

    return {"result": prediction}
