from fastapi import APIRouter, status
from typing import List
from ..models import learnings
from ..data.mongodb.learnings import LearningsDataReader, LearningsDataWriter, LearningDataDeleter
from ..api.learnings import fetch_learnings_api, create_learnings_api, update_learnings_api, delete_learnings_api

router = APIRouter(
	prefix="/learnings",
	tags=["Learnings"],
	responses={404: {"description": "Not found"}}
)

@router.get(
    "/", 
    response_model=List[learnings.Learnings], 
    status_code=status.HTTP_200_OK)
async def fetch_learnings() -> List[learnings.Learnings]:
    ldReader = LearningsDataReader()
    return await fetch_learnings_api(ldReader)

@router.post(
    "/", 
    response_model=learnings.LearningsResponse,
    status_code=status.HTTP_201_CREATED)
async def create_learnings(learningItem: learnings.Learnings):
    ldReader = LearningsDataReader()
    ldWriter = LearningsDataWriter()
    return await create_learnings_api(ldReader, ldWriter, learningItem)

@router.put(
    "/", 
    response_model=learnings.LearningsResponse,
    status_code=status.HTTP_200_OK)
async def update_learnings(learningItem: learnings.Learnings):
    ldReader = LearningsDataReader()
    ldWriter = LearningsDataWriter()
    return await update_learnings_api(ldReader, ldWriter, learningItem)

@router.delete(
	"/",
	status_code=status.HTTP_204_NO_CONTENT)
async def delete_learnings(id: int):
    ldDeleter = LearningDataDeleter()
    return await delete_learnings_api(ldDeleter, id)
