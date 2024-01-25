from fastapi import Depends, FastAPI
import os
from routers import upload

app = FastAPI()
app.include_router(upload.router)


@app.get("/")
async def root():
    return {"Information": "This is the root of the application"}


if __name__ == "__main__":
    import uvicorn

    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", 8000))

    uvicorn.run(app, host=host, port=port, reload=True)
