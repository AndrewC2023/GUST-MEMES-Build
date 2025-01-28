
import random
from typing import Union
from fastapi import FastAPI

# fake drone list
DRONE_IDS = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10
]

app = FastAPI()

#sending stuff with the API
@app.get("/test_data/get_generated_data")
async def generate_data():
    position_array = []
    num_positions = None

    #if no range specified, make it random
    if num_positions is None: 
        num_positions = random.randint(1,25)

    for _ in range(0, num_positions):

        # random position coordinates, longitude, latitude, and Altitude
        rand_long  =  random.uniform( -180,  180 )
        rand_lat   =  random.uniform(  -90,  90  )
        rand_alt   =  random.uniform(    0,  50  )

        position_array.append({
           "long"           : rand_long, 
           "lat"            : rand_lat,
           "alt_meters"     : rand_alt
        })
    
    # convert to json payload
    # websocket messages must be btyes or strings

    payload = {
        "coordinates" : position_array,
        "drone_id"    : random.choice(DRONE_IDS),
        "message"     : "WARNING!: This is randomly generated data!"
    }

    return payload

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}