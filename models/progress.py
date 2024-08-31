from dataclasses import dataclass
from datetime import datetime

@dataclass
class Progress:
    id: int
    weight: float
    body_fat: float
    date: datetime
    waist: float

class ProgressList:
    def __init__(self):
        self.progress_records = []

    def add_progress(self, progress):
        self.progress_records.append(progress)

    def get_progress(self):
        return self.progress_records