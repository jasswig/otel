from opentelemetry import trace
from opentelemetry.trace import Status, StatusCode

from fastapi import FastAPI

app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "Square 3"}
current_span = trace.get_current_span()

@app.get("/calculateSqaure/{number}")
def calculateSqaure(number: int):
    sq =  "number"*"number"
    try:
        int(sq)
        return sq
    except ValueError:
        current_span.set_status(Status(StatusCode.ERROR))
        return sq