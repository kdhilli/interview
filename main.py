from fastapi import FastAPI
from app.routes import router
from app.database import connect_to_mongo, close_mongo_connection

app = FastAPI(title="MongoDB REST API")

# Include routes
app.include_router(router)

# MongoDB connection events
@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()

@app.get("/")
async def root():
    return {"message": "Welcome to the MongoDB REST API"}