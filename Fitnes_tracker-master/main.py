from views.console_view import ConsoleView
from presenters.fitness_presenter import FitnessPresenter

def main():
    view = ConsoleView()
    presenter = FitnessPresenter(view)

    while True:
        choice = view.show_menu()

        if choice == '1':
            workout_type, duration, date, calories = view.get_workout_input()
            presenter.add_workout(workout_type, duration, date, calories)
        elif choice == '2':
            workout_id = int(input("Введите ID тренировки для удаления: "))
            presenter.remove_workout(workout_id)
        elif choice == '3':
            presenter.view_workouts()
        elif choice == '4':
            weight, body_fat, date, waist = view.get_progress_input()
            presenter.add_progress(weight, body_fat, date, waist)
        elif choice == '5':
            presenter.view_progress()
        elif choice == '6':
            presenter.generate_report()
        elif choice == '7':
            presenter.save_data()
        elif choice == '8':
            presenter.load_data()
        elif choice == '9':
            filename = view.get_filename()
            presenter.save_workouts_to_file(filename)
        elif choice == '10':
            filename = view.get_filename()
            presenter.load_workouts_from_file(filename)
        elif choice == '11':
            break
        else:
            view.show_message("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()