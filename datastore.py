# MODULE 2: datastore.py
# This file keeps a simple list in memory.
# Data will be lost when program closes.

expenses_list = []

def add_to_store(expense):
    expenses_list.append(expense)

def get_all():
    return expenses_list

def delete_from_store(index):
    expenses_list.pop(index)

def update_in_store(index, new_expense):
    expenses_list[index] = new_expense

