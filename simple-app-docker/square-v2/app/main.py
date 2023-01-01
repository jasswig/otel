from fastapi import FastAPI
import time
from random import randint

app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "Square 2"}


@app.get("/calculateSqaure/{number}")
def calculateSqaure(number: int):
    time.sleep(randint(1, 10))
    return number*number
