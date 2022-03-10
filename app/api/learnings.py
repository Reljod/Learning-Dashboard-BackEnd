from ..data import ILearningsData

async def fetch_learnings_api(learningsData: ILearningsData, **kwargs):
    return await learningsData.learnings(**kwargs)