import abc
from typing import List
from ..models import learnings

class ILearningsDataReader(abc.ABC):
    @classmethod
    async def fetch(self, item_count: int = -1):
        pass
    
    @classmethod
    async def fetch_recent(self):
        pass
    
    @classmethod
    async def fetch_by_id(self, id):
        pass
    

class ILearningsDataWriter(abc.ABC):
    @classmethod
    async def create(self, learning_item: learnings.Learnings) -> None:
        pass
    
    async def update(self, learning_item: learnings.Learnings) -> learnings.Learnings:
        pass
	

class ILearningsDataDeleter(abc.ABC):
    @classmethod
    async def delete(self, id):
        pass
    
    @classmethod
    async def delete_batch(self, ids: List[int]):
        pass