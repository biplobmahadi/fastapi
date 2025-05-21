from fastapi import APIRouter, HTTPException, Depends

router = APIRouter()

@router.get("/choices/{question_id}")
async def read():
    return {"message": "Hello World"}