from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv


import models,database
import users, weather



models.Base.metadata.create_all(bind=database.engine)

app= FastAPI(title="User & Weather API", docs_url="/docs", redoc_url="/redoc")
print("Fastapi is initializing")

@app.get("/")
def root():
    return {"message":"Welcome to the User & Weather Info Api"}


print("Routers are included")

app.include_router(users.router)
app.include_router(weather.router)