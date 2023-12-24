# Expense Manager

## About the Project
This repository houses a Python-based expense tracking system. Key features include:

**Expense Class:** Represents individual expenses, capturing details such as title, amount, creation date, and update date.

**ExpenseDatabase Class:** Manages a set of expenses, providing functionalities for addition, removal, retrieval, and updating.


## How to clone the repository

1. Open a terminal.

2. Clone the repository to your local machine using the command below:
   ```bash
   git clone https://github.com/awaemma/Alt_School_projects.git

## How to run the code
1. Change the working directory to the Expense_Manager directory
 ```bash
    cd Expense_Manager
 ```
2. run the Expense_and_ExpenseDatabase.py

## Sample Usage
```bash
from expense_tracker import Expense, ExpenseDatabase

# Create an expense database
expense_db = ExpenseDatabase()

# Add expenses
expense_db.add_expense(Expense("Travel", 1000.00))
expense_db.add_expense(Expense("Eatery", 35.50))

# Get expenses by title
grocery_expenses = expense_db.get_expenses_by_title("Travel")

# Print all expenses
print(expense_db.to_dict())


   

