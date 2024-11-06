import firebase_admin
from firebase_admin import credentials, firestore
import time
import config


def current_milli_time():
    return (round(time.time() * 1000))


cred = credentials.Certificate(config.firebase_key_path)
app = firebase_admin.initialize_app(cred)
db = firestore.client()
users_ref = db.collection("users")
loc_ref = db.collection("locations")


def get_db_locations():
    locations = loc_ref.stream()
    arr = []
    for location in locations:
        if current_milli_time() - location.to_dict()["Time"] >= 10000:
            continue
        arr.append(location.to_dict())
    return arr


def put_location(loc):
    print(loc)
    loc["Time"] = current_milli_time()
    loc_ref.document(loc["Id"]).set(loc)
