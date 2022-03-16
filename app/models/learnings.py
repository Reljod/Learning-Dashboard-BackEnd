import enum
import pydantic
from fastapi import status

class StatusEnum(str, enum.Enum):
    Done = "done"
    ToDo = "to do"
    Ongoing = "ongoing"
    
class LearningSource(str, enum.Enum):
    InternetActivity = "Internet Activity"
    SelfNotes = "Self Notes"

class Learnings(pydantic.BaseModel):
    id: int
    title: str
    source: LearningSource
    createdDate: str  # YYYY-MM-DD[T]HH:MM[:SS[.ffffff]] format
    mostRecentUpdate: str  # YYYY-MM-DD[T]HH:MM[:SS[.ffffff]] format
    status: StatusEnum
    body: str
    
    class Config:
        schema_extra = {
            "example": {
                "id": "1",
                "title": "Learning Foo",
                "source": LearningSource.SelfNotes,
                "createdDate": "Mar 13, 2022, 11:58:35 PM",
                "mostRecentUpdate": "Mar 14, 2022, 11:58:35 PM",
                "status": StatusEnum.ToDo,
                "body": "Notes body"
            }
        }

class ActionEnum(str, enum.Enum):
    NoActions = "No Actions"
    Created = "Created New"
    Updated = "Updated"
    
class LearningsResponse(pydantic.BaseModel):
    learnings: Learnings
    action: ActionEnum
    message: str | None