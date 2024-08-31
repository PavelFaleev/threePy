from models.workout import Workout, WorkoutList
from models.progress import Progress, ProgressList
from services.data_handler import DataHandler
from services.report_generator import ReportGenerator

class FitnessPresenter:
    def __init__(self, view):
        self.view = view
        self.workout_list = WorkoutList()
        self.progress_list = ProgressList()
        self.data_handler = DataHandler()
        self.report_generator = ReportGenerator()

    def add_workout(self, workout_type, duration, date, calories):
        workout_id = len(self.workout_list.get_workouts()) + 1
        workout = Workout(workout_id, workout_type, duration, date, calories)
        self.workout_list.add_workout(workout)
        self.view.show_message("Тренировка успешно добавлена.")

    def remove_workout(self, workout_id):
        self.workout_list.remove_workout(workout_id)
        self.view.show_message("Тренировка успешно удалена.")

    def view_workouts(self):
        workouts = self.workout_list.get_workouts()
        self.view.show_workouts(workouts)

    def add_progress(self, weight, body_fat, date, waist):
        progress_id = len(self.progress_list.get_progress()) + 1
        progress = Progress(progress_id, weight, body_fat, date, waist)
        self.progress_list.add_progress(progress)
        self.view.show_message("Прогресс успешно добавлен.")

    def view_progress(self):
        progress_records = self.progress_list.get_progress()
        self.view.show_progress(progress_records)

    def generate_report(self):
        report = self.report_generator.generate_report(self.workout_list, self.progress_list)
        self.view.show_message(report)

    def save_data(self):
        self.data_handler.save_data(self.workout_list, self.progress_list)
        self.view.show_message("Данные успешно сохранены.")

    def load_data(self):
        loaded_data = self.data_handler.load_data()
        if loaded_data:
            self.workout_list, self.progress_list = loaded_data
            self.view.show_message("Данные успешно загружены.")
        else:
            self.view.show_message("Данные не найдены или произошла ошибка при загрузке.")

    def save_workouts_to_file(self, filename):
        self.workout_list.save_to_file(filename)
        self.view.show_message(f"Тренировки сохранены в файл {filename}")

    def load_workouts_from_file(self, filename):
        self.workout_list.load_from_file(filename)
        self.view.show_message(f"Тренировки загружены из файла {filename}")