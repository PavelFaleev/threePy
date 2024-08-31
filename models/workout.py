from dataclasses import dataclass
from datetime import datetime

@dataclass
class Workout:
    id: int
    type: str
    duration: int
    date: datetime
    calories: int

class WorkoutList:
    def __init__(self):
        self.workouts = []

    def add_workout(self, workout):
        self.workouts.append(workout)

    def remove_workout(self, workout_id):
        self.workouts = [w for w in self.workouts if w.id != workout_id]

    def get_workouts(self):
        return self.workouts

    def save_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            for workout in self.workouts:
                file.write(f"{workout.id},{workout.type},{workout.duration},{workout.date},{workout.calories}\n")

    def load_from_file(self, filename):
        self.workouts = []
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                for line in file:
                    id, type, duration, date, calories = line.strip().split(',')
                    self.workouts.append(Workout(int(id), type, int(duration), datetime.fromisoformat(date), int(calories)))
        except FileNotFoundError:
            print(f"Файл {filename} не найден.")