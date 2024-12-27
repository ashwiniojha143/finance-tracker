from data_handler import DataHandler
from analytics import Analytics
from visualization import Visualization

def main():
    print("Welcome to the Personal Finance Tracker!")
    
    # Initialize components
    data_handler = DataHandler()
    analytics = Analytics()
    visualization = Visualization()

    while True:
        print("\nChoose an option:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Visualize Data")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter income amount: "))
            source = input("Enter income source: ")
            data_handler.add_transaction('income', amount, source)

        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            data_handler.add_transaction('expense', amount, category)

        elif choice == '3':
            summary = analytics.calculate_summary(data_handler.transactions)
            print("\n--- Summary ---")
            for key, value in summary.items():
                print(f"{key}: {value}")

        elif choice == '4':
            visualization.plot_expense_pie(data_handler.get_expense_data())

        elif choice == '5':
            print("Thank you for using the Personal Finance Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()