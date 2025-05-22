from fastapi import APIRouter, HTTPException
from app.database import db
from app.models import Record
from app.schemas import RecordCreate

router = APIRouter()

@router.post("/records/", response_model=Record)
async def create_record(record: RecordCreate):
    new_record = record.dict()
    result = await db.records.insert_one(new_record)
    created_record = await db.records.find_one({"_id": result.inserted_id})
    return Record(**created_record)

@router.get("/records/")
async def get_records():
    records = await db.records.find().to_list(100)
    return [Record(**record) for record in records]