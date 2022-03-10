import abc
from ..models import learnings

class ILearningsData(abc.ABC):
    @classmethod
    async def learnings(self, item_count: int = -1):
        pass
    
    @classmethod
    async def recent_learnings(self):
        pass