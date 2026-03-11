from fastapi import FastAPI

from models import Snapshot


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "ingest-api is accessible"}

@app.post("/ingest", status_code=202)
async def ingest(data: Snapshot):
    # print(data.model_dump_json(indent=2))
    return {"status": "ok"}

