from fastapi import APIRouter
from typing import List
from ..models import learnings
from ..data.mongodb.learnings import LearningsData
from ..api.learnings import fetch_learnings_api

router = APIRouter(
	prefix="/learnings",
	tags=["Learnings"],
	responses={404: {"description": "Not found"}}
)

@router.get("/")
async def fetch_learnings() -> List[learnings.Learnings]:
    ldObj = LearningsData()
    return await fetch_learnings_api(ldObj)
    

