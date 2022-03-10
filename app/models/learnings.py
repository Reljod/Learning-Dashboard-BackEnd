import enum
import pydantic

class StatusEnum(str, enum.Enum):
    Done = "done"
    ToDo = "to do"
    Ongoing = "ongoing"

class Learnings(pydantic.BaseModel):
    id: int
    title: str
    source: str
    startDate: str  # YYYY-MM-DD[T]HH:MM[:SS[.ffffff]] format
    mostRecentUpdate: str  # YYYY-MM-DD[T]HH:MM[:SS[.ffffff]] format
    status: StatusEnum