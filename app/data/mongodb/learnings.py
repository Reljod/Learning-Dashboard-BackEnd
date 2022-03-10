from typing import List
from . import get_database, Config
from .. import ILearningsData
from ...models import learnings


class LearningsData(ILearningsData):

    def __init__(self) -> None:
        super().__init__()
        self.learnings_collection = get_database()[Config.LEARNINGS_COLLECTION]

    async def learnings(self, item_count=-1) -> List[learnings.Learnings]:
       learnings_all = self.learnings_collection.find()
       learnings_objs = [self._parse_obj(learning) for learning in learnings_all]
       
       len_learnings = len(learnings_objs)
       if item_count > 0 and item_count < len_learnings:
           return learnings_objs[:item_count]
       
       return learnings_objs

    async def recent_learnings(self):
        return self.learnings(item_count=10)
    
    def _parse_obj(self, learning_data):
        return learnings.Learnings.parse_obj(learning_data)