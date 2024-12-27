class Analytics:
    def calculate_summary(self, transactions):
        total_income = transactions[transactions['type'] == 'income']['amount'].sum()
        total_expenses = transactions[transactions['type'] == 'expense']['amount'].sum()
        savings = total_income - total_expenses

        return {
            'Total Income': total_income,
            'Total Expenses': total_expenses,
            'Savings': savings
        }