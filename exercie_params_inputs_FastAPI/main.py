from fastapi import FastAPI
from pydantic import BaseModel

class Value(BaseModel):
    value: int

# Instantiate the app.
app = FastAPI()

# Define a GET on the specified endpoint.
## path...path parameter --> ist in URL Path enthalten (wird übergeben)
## query...query parameter --> wird mit ? im URL angegeben 
## body...request body --> bedeutet das eine Klasse dafür anlegt wird
@app.post("/{path}")
async def exercise_function(path: int, query: int, body: Value):
    return {"path": path, "query": query, "body": body}