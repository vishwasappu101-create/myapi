from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Vishwa's API + Calculator")

# Serve the 'static' folder as a website at /calc (serves index.html automatically)
app.mount("/calc", StaticFiles(directory="static", html=True), name="calc")

@app.get("/")
def home():
    return {"message": "Hello, Vishwa! Your API and Calculator are live 🚀"}

