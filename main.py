# Import modules
import csv
import sys
import datetime

# Create global variable for csv file
FILENAME = "log.csv"

# Exercise Entry Class
class ExerciseEntry:
    def __init__(self, date, exercise, sets, reps, weight):
        self.date = date
        self.exercise = exercise
        self.sets = sets
        self.reps = reps
        self.weight = weight
        
    # Create iterable object in order to be saved to a csv file
    def __iter__(self, date, exercise, sets, reps, weight):
        return iter([self.date, self.exercise, self.sets, self.reps, self.weight])
        

# Exercise Tracker Class
class ExerciseLog:
    def __init__(self):
        self.entries = []
        
    # Add a new exercise entry
    def add_entry(self, entry):
        self.entries.append(entry)
        print("Entry added.")

    # Delete an existing exercise entry
    def delete_entry(self, index):
        if 0 <= index < len(self.entries):
            del self.entries[index]
            print("Entry deleted.")
        else:
            print("There's nothing to delete.")

    # Edit an existing exercise entry
    def edit_entry(self, index, new_entry):
        if 0 <= index < len(self.entries):
            self.entries[index] = new_entry
            print("Entry updated.")
        else:
            print("There's nothing to update.")

    # Review recently entered exercise entries
    def review_entries(self):
        for i, entry in enumerate(self.entries):
            print(f"Entry {i + 1}: Date: {entry.date}, Exercise: {entry.exercise}, "
                  f"Sets: {entry.sets}, Reps : {entry.reps}, Weight: {entry.weight}")

    # Save the entire exercise log to a file
    def save_log(self, log):
        # Use try/exception here to notify user if file is not found
        try:
            with open(FILENAME, 'a') as csv_file:
                wr = csv.writer(csv_file, delimiter=',')
                for entry in self.entries:
                    wr.writerow([entry.date, entry.exercise, 
                             entry.sets, entry.reps, entry.weight])
        except Exception as e:
            print(type(e), e)
            sys.exit()
            
    # Confirm the user wants to exit the program
    def confirm_exit(self):
        print("Exiting does not save entries to the log.")
        print("Are you sure you want to exit?")
        exit = input("(Y/N): ").upper()
        if exit == "Y":
            sys.exit()
        else:
            print("Returning to main menu.")
            main()


# Define main program loop
def main():
    log = ExerciseLog()

    while True:
        print("Options: add, delete, edit, review, save, exit")
        option = input("Choose an option: ").lower()

        if option == "add":
            date = datetime.date.today().strftime("%m-%d-%Y")
            exercise = input("Enter exercise: ")
            sets = input("Enter sets: ")
            reps = input("Enter repetitions: ")
            weight = input("Enter weight: ")
            entry = ExerciseEntry(date, exercise, sets, reps, weight)
            log.add_entry(entry)

        elif option == "edit":
            index = int(input("Enter which entry number to edit: ")) - 1
            date = input("Enter new date: ")
            exercise = input("Enter new exercise: ")
            sets = input("Enter new sets: ")
            reps = input("Enter new repetitions: ")
            weight = input("Enter new weight: ")
            new_entry = ExerciseEntry(date, exercise, sets, reps, weight)
            log.edit_entry(index, new_entry)

        elif option == "delete":
            index = int(input("Enter which entry you want to delete: "))
            log.delete_entry(index)

        elif option == "review":
            log.review_entries()

        elif option =="save":
            log.save_log(log)
            
        elif option == "exit":
            log.confirm_exit()
            break

        else:
            print("Invalid option. Please try again.")

    

if __name__ == "__main__":
    main()