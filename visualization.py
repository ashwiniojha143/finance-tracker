import matplotlib.pyplot as plt

class Visualization:
    def plot_expense_pie(self, expenses):
        categories = list(expenses.keys())
        amounts = list(expenses.values())

        plt.figure(figsize=(8, 8))
        plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
        plt.title('Expense Breakdown')
        plt.show()