from fastapi import FastAPI
import uvicorn
from pyspark.sql import SparkSession
from pyspark.ml.classification import RandomForestClassificationModel

app = FastAPI()
spark = SparkSession.builder.getOrCreate()

model = RandomForestClassificationModel.load('./model')

@app.get('/')
def main():
    return {"Hello World"}

@app.get('/prediction')
def prediction():
    return {"Prediction goes here"}
    
if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)