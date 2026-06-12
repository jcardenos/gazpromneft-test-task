from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/")
async def receive(request: Request):
    body = await request.body()
    print(body.decode("utf-8", errors="ignore"))
    return {"status": "ok"}
