class ReportGenerator:
    def generate_report(self, workout_list, progress_list):
        total_workouts = len(workout_list.get_workouts())
        total_duration = sum(w.duration for w in workout_list.get_workouts())
        total_calories = sum(w.calories for w in workout_list.get_workouts())
        
        if progress_list.get_progress():
            initial_weight = progress_list.get_progress()[0].weight
            current_weight = progress_list.get_progress()[-1].weight
            weight_change = current_weight - initial_weight
            
            initial_body_fat = progress_list.get_progress()[0].body_fat
            current_body_fat = progress_list.get_progress()[-1].body_fat
            body_fat_change = current_body_fat - initial_body_fat
            
            initial_waist = progress_list.get_progress()[0].waist
            current_waist = progress_list.get_progress()[-1].waist
            waist_change = current_waist - initial_waist
        else:
            weight_change = body_fat_change = waist_change = 0

        report = f"Общее количество тренировок: {total_workouts}\n"
        report += f"Общая продолжительность тренировок: {total_duration} минут\n"
        report += f"Общее количество сожженных калорий: {total_calories}\n"
        report += f"Изменение веса: {weight_change:.2f} кг\n"
        report += f"Изменение процента жира: {body_fat_change:.2f}%\n"
        report += f"Изменение обхвата талии: {waist_change:.2f} см"

        return report