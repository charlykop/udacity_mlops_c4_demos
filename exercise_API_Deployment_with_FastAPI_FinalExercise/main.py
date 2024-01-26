from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Data(BaseModel):
    feature_1: float
    feature_2: str

app = FastAPI()

@app.post("/data/")
async def input_data(data: Data):
    if data.feature_1 < 0:
        raise HTTPException(status_code=422, detail='feature_1 needs to be positiv.')
    if len(data.feature_2) > 280:
        raise HTTPException(status_code=422, detail='feature_2 need to be smaller then 280 characters.')
    return data

