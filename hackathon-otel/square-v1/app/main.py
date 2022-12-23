from fastapi import FastAPI

app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "Square 1"}


@app.get("/calculateSqaure/{number}")
def fetch_from_app1(number: int):
    return number*number
