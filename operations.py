# MODULE 3: operations.py

from expense import Expense
import datastore

def add_expense():
    print("\n--- Add Expense ---")
    amount = input("Amount: ")
    category = input("Category: ")
    date = input("Date (DD-MM-YYYY): ")
    note = input("Note: ")

    e = Expense(amount, category, date, note)
    datastore.add_to_store(e)

    print("Expense added.")

def show_expenses():
    print("\n--- All Expenses ---")
    data = datastore.get_all()

    if len(data) == 0:
        print("No expenses yet.")
        return

    for i, e in enumerate(data):
        print(f"{i+1}. {e.amount} | {e.category} | {e.date} | {e.note}")

def update_expense():
    data = datastore.get_all()
    show_expenses()

    if len(data) == 0:
        return

    pos = int(input("Enter number to update: ")) - 1
    old = data[pos]

    print("Press enter to keep old value.")

    amt = input(f"New amount ({old.amount}): ")
    cat = input(f"New category ({old.category}): ")
    dt = input(f"New date ({old.date}): ")
    nt = input(f"New note ({old.note}): ")

    if amt == "":
        amt = old.amount
    if cat == "":
        cat = old.category
    if dt == "":
        dt = old.date
    if nt == "":
        nt = old.note

    new_e = Expense(amt, cat, dt, nt)
    datastore.update_in_store(pos, new_e)

    print("Updated.")

def delete_expense():
    data = datastore.get_all()
    show_expenses()

    if len(data) == 0:
        return

    pos = int(input("Enter number to delete: ")) - 1
    datastore.delete_from_store(pos)
    print("Deleted.")
