from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app = FastAPI(title="Vishwa's Calculator API")

# Serve the calculator from the /calc route
app.mount("/calc", StaticFiles(directory="static", html=True), name="calc")

# Redirect root (/) to /calc automatically
@app.get("/")
def root():
    return RedirectResponse(url="/calc")
