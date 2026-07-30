# ======================================
# Personal Expense Tracker
# Part 1 - Project Setup & Main Menu
# ======================================

# List to store all expenses
expenses = []


# ---------- Functions ----------

def main_menu():
    print("\n=================================")
    print("     PERSONAL EXPENSE TRACKER")
    print("=================================")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Edit Expense")
    print("4. Delete Expense")
    print("5. Search Expense")
    print("6. Category Summary")
    print("7. Total Spending")
    print("8. Exit")


def add_expense():

    print("\n===== Add Expense =====")

    title = input("Enter Expense Title: ")

    category = input("Enter Category: ")

    while True:
        try:
            amount = float(input("Enter Amount: "))
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")

    date = input("Enter Date (DD/MM/YYYY): ")

    expense = {
        "title": title,
        "category": category,
        "amount": amount,
        "date": date
    }

    expenses.append(expense)

    print("\nExpense added successfully!")


def view_expenses():

    print("\n===== View Expenses =====")

    if len(expenses) == 0:
        print("No expenses found.")
        return

    print("\n-----------------------------------------------------------")
    print("No.  Title            Category        Amount        Date")
    print("-----------------------------------------------------------")

    for i in range(len(expenses)):

        print(f"{i+1:<4}"
              f"{expenses[i]['title']:<17}"
              f"{expenses[i]['category']:<16}"
              f"{expenses[i]['amount']:<14.2f}"
              f"{expenses[i]['date']}")

    print("-----------------------------------------------------------")


def edit_expense():

    print("\n===== Edit Expense =====")

    if len(expenses) == 0:
        print("No expenses found.")
        return

    # Display all expenses
    view_expenses()

    while True:
        try:
            number = int(input("\nEnter expense number to edit: "))

            if 1 <= number <= len(expenses):
                break
            else:
                print("Invalid expense number.")

        except ValueError:
            print("Please enter a valid number.")

    index = number - 1

    print("\nEnter new details")

    expenses[index]["title"] = input("Enter Expense Title: ")
    expenses[index]["category"] = input("Enter Category: ")

    while True:
        try:
            expenses[index]["amount"] = float(input("Enter Amount: "))
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")

    expenses[index]["date"] = input("Enter Date (DD/MM/YYYY): ")

    print("\nExpense updated successfully!")


def delete_expense():

    print("\n===== Delete Expense =====")

    if len(expenses) == 0:
        print("No expenses found.")
        return

    # Display all expenses
    view_expenses()

    while True:
        try:
            number = int(input("\nEnter expense number to delete: "))

            if 1 <= number <= len(expenses):
                break
            else:
                print("Invalid expense number.")

        except ValueError:
            print("Please enter a valid number.")

    confirm = input("Are you sure? (Y/N): ")

    if confirm.upper() == "Y":

        deleted = expenses.pop(number - 1)

        print(f"\n'{deleted['title']}' has been deleted successfully!")

    else:
        print("\nDeletion cancelled.")


def search_expense():

    print("\n===== Search Expense =====")

    if len(expenses) == 0:
        print("No expenses found.")
        return

    keyword = input("Enter expense title or category: ").lower()

    found = False

    print("\n-----------------------------------------------------------")
    print("No.  Title            Category        Amount        Date")
    print("-----------------------------------------------------------")

    for i in range(len(expenses)):

        if (keyword in expenses[i]["title"].lower()) or \
           (keyword in expenses[i]["category"].lower()):

            print(f"{i+1:<4}"
                  f"{expenses[i]['title']:<17}"
                  f"{expenses[i]['category']:<16}"
                  f"{expenses[i]['amount']:<14.2f}"
                  f"{expenses[i]['date']}")

            found = True

    print("-----------------------------------------------------------")

    if found == False:
        print("No matching expenses found.")


def category_summary():

    print("\n===== Category Summary =====")

    if len(expenses) == 0:
        print("No expenses found.")
        return

    categories = {}

    # Calculate total for each category
    for expense in expenses:

        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    print("\n------------------------------")
    print("Category           Total")
    print("------------------------------")

    for category, total in categories.items():
        print(f"{category:<18}{total:.2f}")

    print("------------------------------")


def total_spending():

    print("\n===== Total Spending =====")

    if len(expenses) == 0:
        print("No expenses found.")
        return

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\nYour Total Spending is: {total:.2f}")


# ---------- Main Program ----------

while True:

    main_menu()

    choice = input("\nEnter your choice (1-8): ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        edit_expense()

    elif choice == "4":
        delete_expense()

    elif choice == "5":
        search_expense()

    elif choice == "6":
        category_summary()

    elif choice == "7":
        total_spending()

    elif choice == "8":
        print("\nThank you for using Personal Expense Tracker!")
        break

    else:
        print("\nInvalid choice. Please try again.")