import datetime

from ..data import ILearningsDataReader, ILearningsDataWriter, ILearningsDataDeleter
from ..models import learnings

async def fetch_learnings_api(learnings_data: ILearningsDataReader, **kwargs):
    return await learnings_data.fetch(**kwargs)

async def create_learnings_api(
    learnings_reader: ILearningsDataReader,
    learnings_writer: ILearningsDataWriter,
    learnings_item: learnings.Learnings
    ) -> learnings.LearningsResponse:
    
    learning_fetched_item = await learnings_reader.fetch_by_id(learnings_item.id)
    
    def build_response(l_item, l_action):
        learnings_response = learnings.LearningsResponse(
            learnings=l_item,
            action=l_action
        )
        return learnings_response
    
    if learning_fetched_item is not None:
        response = build_response(learnings_item, learnings.ActionEnum.NoActions)
        response.message = "Already existing"
        return response

    await learnings_writer.create(learnings_item)
    
    response = build_response(learnings_item, learnings.ActionEnum.Created)
    response.message = "Learning item created"
    return response

async def update_learnings_api(
    learnings_reader: ILearningsDataReader,
    learnings_writer: ILearningsDataWriter,
    learnings_item: learnings.Learnings
    ) -> learnings.LearningsResponse:
    
    learning_fetched_item = await learnings_reader.fetch_by_id(learnings_item.id)
    
    def build_response(l_item, l_action):
        learnings_response = learnings.LearningsResponse(
            learnings=l_item,
            action=l_action
        )
        
        return learnings_response
    
    if learning_fetched_item is None:
        response = build_response(learnings_item, learnings.ActionEnum.NoActions)
        response.message = "Item does not exists"
        return response
    
    # most_recent_update = learnings_item.mostRecentUpdate
    
    updated_learning_item = await learnings_writer.update(learnings_item)
    
    response = build_response(updated_learning_item, learnings.ActionEnum.Updated)
    response.message = "Learning item updated"
    return response

async def delete_learnings_api(learnings_deleter: ILearningsDataDeleter, id: int) -> None:
    return await learnings_deleter.delete(id)


# def correct_date(learning_item: learnings.Learnings):
    
#     most_recent_update = datetime.datetime.fromisoformat(learning_item.mostRecentUpdate)
#     created_date = datetime.datetime.fromisoformat(learning_item.createdDate)
    
#     return learnings.Learnings(
#         **learning_item, 
#         mostRecentUpdate= 
#     )
    
    