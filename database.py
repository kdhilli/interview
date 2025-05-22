from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb+srv://admin:<db_password>@cluster0.auch0y2.mongodb.net/"
MONGO_DB_NAME = "test_db"

client = None
db = None

async def connect_to_mongo():
    global client, db
    client = AsyncIOMotorClient(MONGO_URI)
    db = client[MONGO_DB_NAME]
    print("Connected to MongoDB")

async def close_mongo_connection():
    global client
    if client:
        client.close()
        print("Closed MongoDB connection")