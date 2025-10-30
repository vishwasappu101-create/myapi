from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app = FastAPI(title="Vishwa's Calculator API")

app.mount("/calc", StaticFiles(directory="static", html=True), name="calc")

@app.get("/")
def root():
    return RedirectResponse(url="/calc")
