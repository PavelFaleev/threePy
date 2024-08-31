from datetime import datetime

class ConsoleView:
    def show_menu(self):
        print("\n1. Добавить тренировку")
        print("2. Удалить тренировку")
        print("3. Просмотреть тренировки")
        print("4. Добавить прогресс")
        print("5. Просмотреть прогресс")
        print("6. Сгенерировать отчет")
        print("7. Сохранить данные")
        print("8. Загрузить данные")
        print("9. Сохранить тренировки в файл")
        print("10. Загрузить тренировки из файла")
        print("11. Выход")
        return input("Выберите опцию: ")

    def get_workout_input(self):
        workout_type = input("Введите тип тренировки: ")
        duration = int(input("Введите продолжительность (в минутах): "))
        calories = int(input("Введите количество сожженных калорий: "))
        date = datetime.now()
        return workout_type, duration, date, calories

    def get_progress_input(self):
        weight = float(input("Введите вес (кг): "))
        body_fat = float(input("Введите процент жира: "))
        waist = float(input("Введите обхват талии (см): "))
        date = datetime.now()
        return weight, body_fat, date, waist

    def show_workouts(self, workouts):
        for workout in workouts:
            print(f"ID: {workout.id}, Тип: {workout.type}, Продолжительность: {workout.duration} минут, Дата: {workout.date}, Калории: {workout.calories}")

    def show_progress(self, progress_records):
        for progress in progress_records:
            print(f"ID: {progress.id}, Вес: {progress.weight} кг, Процент жира: {progress.body_fat}%, Дата: {progress.date}, Обхват талии: {progress.waist} см")

    def show_message(self, message):
        print(message)

    def get_filename(self):
        return input("Введите имя файла: ")