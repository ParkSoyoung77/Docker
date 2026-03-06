import fastapi, uvicorn

app = fastapi.FastAPI()
@app.get("/")
async def read_root():
    return {"message": "Hello World!"}

# if __nama__ == "__main__":
#       uvicorn.run("main:app", host='0.0.0.0', port=8000m reload=True)