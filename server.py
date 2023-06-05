import uvicorn
from fastapi import *
from fastapi.staticfiles import StaticFiles
from starlette.responses import *  # fastAPI is based off starlette
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="src/html")

@app.get("/")
async def root():
    return FileResponse(f"index.html")

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8080)