import datetime
from database import *

def main_menu():
    """
    Display the main menu. Return the selected option.
    """
    print("Roster Main Menu")
    print("====================================")
    print("Today's date: " + str(datetime.date.today()))
    print("====================================\n")

    print("[T] View or manage tasks.")
    print("[P] View or manage people.")

    print("\n[Q] Quit the program.\n")
    response = input("Enter your choice: ")
    print("\n")
    return response.lower()



def tasks_menu():
    """
    Display the tasks menu. Return the selected option.
    """
    print("Roster Tasks Menu")
    print("====================================")
    print("Today's date: " + str(datetime.date.today()))
    print("====================================\n")
    print("Here are all tasks:")

    for row in db.execute("SELECT * FROM tasks;"):
        print(row)

    print("[A] Add a task.")
    print("[M] Go to main menu.")
    response = input("Enter your choice: ")
    print("\n")
    return response.lower()
