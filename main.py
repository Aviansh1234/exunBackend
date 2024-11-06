from fastapi import FastAPI
import firebase_db as db

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/getLocations")
async def get_locations():
    return db.get_db_locations()

@app.get("/sendLocation")
async def get_locations(location: dict):
    print(type(location))
    print(eval(location))
    db.put_location(location)
    return "ok"