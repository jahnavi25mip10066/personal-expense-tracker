# MODULE 5: main.py

from display import menu
import operations

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        operations.add_expense()
    elif choice == "2":
        operations.show_expenses()
    elif choice == "3":
        operations.update_expense()
    elif choice == "4":
        operations.delete_expense()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option")
