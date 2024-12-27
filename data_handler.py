import pandas as pd

class DataHandler:
    def __init__(self):
        self.transactions = pd.DataFrame(columns=['type', 'amount', 'category_or_source'])

    def add_transaction(self, t_type, amount, category_or_source):
        new_transaction = {'type': t_type, 'amount': amount, 'category_or_source': category_or_source}
        self.transactions = pd.concat([self.transactions, pd.DataFrame([new_transaction])], ignore_index=True)

    def get_expense_data(self):
        expenses = self.transactions[self.transactions['type'] == 'expense']
        return expenses.groupby('category_or_source')['amount'].sum().to_dict()