from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="DocQuest Backend", version="0.1.0")

@app.get("/healthz")
async def healthz():
    return JSONResponse({"ok": True})

@app.get("/readyz")
async def readyz():
    # TODO: check DB connections, etc.
    return JSONResponse({"ready": True})
