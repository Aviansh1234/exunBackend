from fastapi import FastAPI
import firebase_db as db
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "*"
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/sendLocation")
async def set_location(latitude: float, longitude: float, id: str):
    location = {"Latitude": latitude, "Longitude": longitude, "Id": id}
    print("here ahhhh")
    print(location)
    db.put_location(location)
    return "ok"

@app.get("/getLocations")
async def get_locations():
    return db.get_db_locations()
