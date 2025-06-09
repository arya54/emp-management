from fastapi import FastAPI
from routes import employees

app = FastAPI(title="Employee Management API")

app.include_router(employees.router)

@app.get("/", include_in_schema=False)
def read_root():
    return {"message": "Welcome to the Employee Management API"}
