import uuid
from datetime import datetime, timezone

class Expense:
    def __init__(self, title, amount):
        """
        This initializes the expense object
        """
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.created_at = self.updated_at = datetime.now(timezone.utc)

    def update(self, title=None, amount=None):
        """
        Allows updating the title and/or amount, and updating the updated_at timestamp
        """
        if title is not None:
            self.title = title
        if amount is not None:
            self.amount = amount
        self.updated_at = datetime.now(timezone.utc)

    def to_dict(self):
        """
        Returns a dictionary representation of the expense
        """
        return {
            'id': self.id,
            'title': self.title,
            'amount': self.amount,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class ExpenseDatabase:
    def __init__(self):
        """
        Initializes the expense list
        """
        self.expenses = []

    def add_expense(self, expense):
        """
        Adds an expense to the database
        """
        self.expenses.append(expense)

    def remove_expense(self, expense_id):
        """
        Removes an expense from the database
        """
        self.expenses = [e for e in self.expenses if e.id != expense_id]

    def get_expense_by_id(self, expense_id):
        """
        Retrieves an expense from the database by the expense_id
        """
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None

    def get_expenses_by_title(self, expense_title):
        """
        Retrieves an expense from the database using it's expense_title
        """
        return [expense for expense in self.expenses if expense.title == expense_title]

    def to_dict(self):
        """
        Method that returns a dictionary representation of the expense.
        """
        return [expense.to_dict() for expense in self.expenses]
