import os
from dotenv import load_dotenv

load_dotenv()

class Config:
	DATABASE_URL = os.environ["DATABASE_URL"]
	DATABASE_NAME = "LearningDashboardAPI"
	LEARNINGS_COLLECTION = "Learning Dashboard"