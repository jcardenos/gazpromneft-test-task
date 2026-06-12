from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import PlainTextResponse
import subprocess

app = FastAPI(title="Task09 WebApp", version="1.0")


@app.post("/", response_class=PlainTextResponse)
async def hello(test: str | None = Header(default=None, alias="Test")):
    if test != "Hello":
        raise HTTPException(status_code=403, detail="Forbidden")
    return "Hello, World!"


@app.get("/health", response_class=PlainTextResponse)
async def health():
    result = subprocess.run(
        ["ping", "-c", "1", "-W", "2", "77.88.8.8"],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        raise HTTPException(status_code=503, detail="Unhealthy")

    return "OK"