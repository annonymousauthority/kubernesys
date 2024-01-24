from fastapi import Depends, FastAPI

from routers import upload

app = FastAPI()
app.include_router(upload.router)


@app.get("/")
async def root():
    return {"Information": "This is the root of the application"}
