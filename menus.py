import datetime
from database import *
from tasks import *

def main_menu():
    """
    Display the main menu and respond to the user's choice.
    """
    print("Roster Main Menu")
    print("====================================")
    print("Today's date: " + str(datetime.date.today()))
    print("====================================\n")

    print("[T] View or manage tasks.")
    print("[P] View or manage people.")

    print("\n[Q] Quit the program.\n")
    response = input("Enter your choice: ").lower()
    print("\n")

    if response == "t":
        tasks_menu()
    elif response == "q":
        return


def tasks_menu():
    """
    Display the tasks menu and responds to the user's choice.
    """
    print("Roster Tasks Menu")
    print("====================================")
    print("Today's date: " + str(datetime.date.today()))
    print("====================================\n")
    print("Here are all tasks:")

    for row in db.execute("SELECT * FROM tasks;"):
        print(row)

    print("\n")
    print("[A] Add a task.")
    print("[M] Go back to the main menu.\n")
    response = input("Enter your choice: ").lower()
    print("\n")

    if response == "a":
        add_task()
        tasks_menu()
    elif response == "m":
        main_menu()


    
