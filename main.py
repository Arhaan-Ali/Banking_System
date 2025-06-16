from bank import Bank
from customer import Customer

def main():
    bank = Bank()

    while True:
        print("\n==== Bank Menu ====")
        print("1. Add Customer")
        print("2. Remove Customer")
        print("3. Create Account")
        print("4. Deposit")
        print("5. Withdraw")
        print("6. Transfer")
        print("7. View Customer Accounts")
        print("8. View All Customers")
        print("9. View All Accounts")
        print("10. Apply interest to Savings Accounts")
        print("11. Exit")

        choice = input("Enter your choice (1-11)")

        if choice == '1':
            customer_id = input("Customer ID: ")
            name = input("Customer Name: ")
            address = input("Customer Address:")
            customer = Customer(customer_id, name, address)
            if bank.AddCustomer(customer):
                print("Customer added successfully")
            else :
                print("Customer ID exists")

        elif choice == '2':
            customer_id = input("Enter Customer ID to remove: ")
            if bank.RemoveCustomer(customer_id):
                print("Customer Removed")
            else:
                print("Customer not removed")

        elif choice == '3':
            customer_id = input("Customer ID: ")
            account_type = input("Account Type (savings/checking) : ")
            initial_balance = float(input("Initial Balance: "))

            if account_type == "savings":
                interest_rate = float(input("Interest Rate: "))
                account = bank.create_account(customer_id, account_type, initial_balance, interest_rate=interest_rate)
            elif account_type == "checking":
                overdraft_limit = float(input("Overdraft Limit: "))
                account = bank.create_account(customer_id, account_type, initial_balance,
                                              overdraft_limit=overdraft_limit)
            else:
                print("❌ Invalid account type.")
                continue

            if account:
                print(
                    f"✅ {account_type.capitalize()} account created successfully. Account No: {account.account_number}")
            else:
                print("❌ Failed to create account.")

        elif choice == '4':
            acc_no = input("Account Number: ")
            amount = float(input("Amount to deposit: "))
            if bank.deposit(acc_no, amount):
                print("✅ Deposit successful.")
            else:
                print("❌ Deposit failed.")

        elif choice == '5':
            acc_no = input("Account Number: ")
            amount = float(input("Amount to withdraw: "))
            if bank.withdraw(acc_no, amount):
                print("✅ Withdrawal successful.")
            else:
                print("❌ Withdrawal failed.")

        elif choice == '6':
            from_acc = input("From Account Number: ")
            to_acc = input("To Account Number: ")
            amount = float(input("Amount to transfer: "))
            if bank.transfer_funds(from_acc, to_acc, amount):
                print("✅ Transfer successful.")
            else:
                print("❌ Transfer failed.")

        elif choice == '7':
            customer_id = input("Customer ID: ")
            accounts = bank.get_customer_accounts(customer_id)
            if not accounts:
                print("❌ No accounts found.")
            else:
                for acc in accounts:
                    acc.display_details()

        elif choice == '8':
            bank.display_all_customers()

        elif choice == '9':
            bank.display_all_accounts()

        elif choice == '10':
            bank.apply_all_interest()
            print("✅ Interest applied to all Savings Accounts.")

        elif choice == '11':
            print("Thank you for using the Banking System. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()


