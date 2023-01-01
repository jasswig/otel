from typing import Union
import requests
from fastapi import FastAPI
import time
from random import randint

app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "from distributor app"}


@app.post("/distribute/{number}")
def distribute(number: int):
    roll_dice = randint(1, 3)
    if roll_dice == 1:
        response = requests.get(url="http://square-v1:5001/calculateSqaure/" + str(number))
    elif roll_dice == 2:
        response = requests.get(url="http://square-v2:5001/calculateSqaure/" + str(number))
    else:
        response = requests.get(url="http://square-v3:5001/calculateSqaure/" + str(number))   
     
    return response.text

