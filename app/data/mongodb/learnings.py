from typing import Dict, List

from . import get_database, Config
from .. import ILearningsDataDeleter, ILearningsDataReader, ILearningsDataWriter
from ...models import learnings

class LearningsDataMongoBase:
    def __init__(self) -> None:
        super().__init__()
        self.learnings_collection = get_database()[Config.LEARNINGS_COLLECTION]
        
    def _parse_obj(self, learning_data):
        return learnings.Learnings.parse_obj(learning_data)
    
    def _to_dict(self, learning_item: learnings.Learnings) -> Dict:
        return learning_item.dict()

class LearningsDataReader(ILearningsDataReader, LearningsDataMongoBase):

    async def fetch(self, item_count=-1) -> List[learnings.Learnings]:
       learnings_all = self.learnings_collection.find()
       learnings_objs = [self._parse_obj(learning)
                                         for learning in learnings_all]

       len_learnings = len(learnings_objs)
       if item_count > 0 and item_count < len_learnings:
           return learnings_objs[:item_count]

       return learnings_objs

    async def fetch_recent(self):
        return self.fetch(item_count=10)

    async def fetch_by_id(self, id) -> learnings.Learnings | None:
        learning = self.learnings_collection.find_one({"id": id})
        if not learning:
            return None
        learning_obj = self._parse_obj(learning)
        return learning_obj
    
    
class LearningsDataWriter(ILearningsDataWriter, LearningsDataMongoBase):
    
    async def create(self, learning_item: learnings.Learnings) -> None: 
        learning_dict = self._to_dict(learning_item)
        self.learnings_collection.insert_one(learning_dict)
        
    async def update(self, learning_item: learnings.Learnings) -> learnings.Learnings | None:
        learning_dict = self._to_dict(learning_item)
        result = self.learnings_collection.update_one(
			{"id": learning_item.id},
			{"$set": learning_dict}
		)
        
        if result and result.matched_count == 0:
            return None
        
        update_learnings_item = self.learnings_collection.find_one({"id": learning_item.id})
        return self._parse_obj(update_learnings_item)


class LearningDataDeleter(ILearningsDataDeleter, LearningsDataMongoBase):
    
    async def delete(self, id: int) -> None:
        self.learnings_collection.delete_one({"id": id})
        
    async def delete_batch(self, ids: List[int]) -> None:
        self.learnings_collection.delete_many({
			"id": {
				"$in": ids
			}
		})