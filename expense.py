# MODULE 1: expense.py
# This class only holds the details of one expense.

class Expense:
    def __init__(self, amount, category, date, note):
        self.amount = amount
        self.category = category
        self.date = date
        self.note = note
