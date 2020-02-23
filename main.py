from database import *
import datetime
from menus import *

create_tables()

while True:
    response = main_menu()
    if response == "q":
        break
    elif response == "t":
        response = tasks_menu()

close_connection()

