from database import *
import datetime

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
    return response.lower()



create_tables()

while True:
    response = main_menu()
    if response == "q":
        break

close_connection()

