import pickle

class DataHandler:
    def save_data(self, workout_list, progress_list):
        with open('fitness_data.pkl', 'wb') as file:
            pickle.dump((workout_list, progress_list), file)

    def load_data(self):
        try:
            with open('fitness_data.pkl', 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return None