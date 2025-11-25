# Personal Expense Tracker

A simple and beginner-friendly Python project that helps track daily expenses in an organised way.  
I built this project to understand how real applications manage data and how CRUD operations work behind the scenes.  
The project is fully menu-driven and runs in the terminal, making it easy to test and use.

---

# 1. Project Overview

Many of us spend money throughout the day without realising where it all goes — small snacks, travel, recharge, online purchases, etc. By the end of the week or month, when we try to recall our spending, it becomes confusing.

This project solves that problem by allowing the user to **record every expense in the moment**, so that their spending is always tracked. The system works directly in the terminal and stores all expenses **temporarily in a list** while the program is running (no permanent files or databases used).

The aim was to keep the project:
- Simple  
- Easy to understand  
- Fast to execute  
- Beginner-friendly  
- Useful for learning modular programming  

---

# 2. Main Features

 Add new expenses  
 View all recorded expenses  
 Update any existing expense  
 Delete selected expenses  
 Completely menu-based interface  
 Clean modular code (multiple Python files)  
 No external libraries required  
 Uses Python lists to store expenses  
 Works in any terminal/IDE  

Each feature has been written in a human-friendly and readable way so that learning is easier.

---

# 3. Technologies & Concepts Used

### Python Concepts:
- Functions  
- Lists  
- Dictionaries  
- Classes & Objects  
- Separate modules (`expense.py`, `operations.py`, etc.)  
- User input handling  
- Loops and conditionals  
- Menu-driven program structure  

### Tools:
- Python 3.10+  
- VS Code / Jupyter / Terminal / Any IDE  
- Git & GitHub for version control  

---

# 4. Project Folder Structure

This project follows a very clean structure so that each file has a clear purpose:
personal-expense-tracker/
│
├── main.py → Starting point of the program
├── expense.py → Defines the Expense class
├── operations.py → Functions for Add/Show/Update/Delete
├── datastore.py → Stores the expenses list
├── display.py → Menu + display formatting
│
├── README.md → Complete project documentation
├── statement.md → Problem statement + scope

#  6. How to Test the Project

Testing the project is very easy:

### 1. Test Adding Expenses  
Choose **1** → Add a few sample expenses.

### 2. Test Viewing Expenses  
Choose **2** → Check if they appear correctly.

### 3. Test Updating an Entry  
Choose **3** → Select an expense and modify it.

### 4. Test Deleting an Expense  
Choose **4** → Remove one entry and confirm list updates.

### 5. Test Exit  
Choose **5** → Program closes safely.

# 8. Purpose of the Project

The main intention behind building this project was to:

- Practice Python fundamentals  
- Learn how to structure projects using modules  
- Understand CRUD operations  
- Improve problem-solving skills  
- Get comfortable with GitHub and documentation  
- Create a real working application instead of short code snippets  

This project reflects genuine learning rather than AI-heavy implementation.


# 9. Future Improvements

If I extend this project later, I would like to add:

- Saving data permanently in a text or JSON file  
- Monthly spending summary  
- Category-wise spending analysis  
- Graphs for visual reports  
- A GUI version using Tkinter  
- Exporting data to Excel or CSV  



# 10. Acknowledgements

This project was built using:
- My Python class notes  
- Basic documentation from python.org  
- GitHub guides  
- My own experimentation, debugging, and practice  

I kept the project simple and human-written to reflect my own understanding of Python.


