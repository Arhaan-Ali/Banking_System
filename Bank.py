import json
from account import SavingsAccount, CheckingAccount
from customer import Customer
class Bank:
    def __init__(self, customer_file = 'customers.json' , account_file = 'accounts.json'):
        self._customers = {}
        self._accounts = {}
        self.customer_file = customer_file
        self.account_file = account_file
        self._load_data()

    def _load_data(self):
        try :
            with open(self.customer_file, "r") as f:
                customers_data = json.load(f)
                for c in customers_data:
                    customer = Customer(
                        c['customer_id'],
                        c['name'],
                        c['address']
            )
            # Add their account_numbers back
                for acc_no in c.get('account_numbers', []):
                    customer.add_account_number(acc_no)

                self._customers[customer.customer_id] = customer
        except FileNotFoundError:
            pass

        try:
            with open(self.account_file, 'r') as f:
                accounts_data = json.load(f)
                for a in accounts_data:
                    acc_type = a.get("type")
                    if acc_type == "savings":
                        account = SavingsAccount(
                            a["account_number"],
                            a["account_holder_id"],
                            a["balance"],
                            a["interest_rate"]
                        )
                    elif acc_type == "checking":
                        account = CheckingAccount(
                            a["account_number"],
                            a["account_holder_id"],
                            a["balance"],
                            a["overdraft_limit"]
                        )
                    else:
                        continue  # skip unknown account types

                    self._accounts[account._account_number] = account
        except FileNotFoundError:
            pass

    def _save_data(self):
        pass

    def AddCustomer(self):
        pass

    def RemoveCustomer(self):
        pass

    def create_account(self, customer_id: str, account_type: str, initial_balance: float = 0.0, **kwargs):
        pass

    def deposit(self, account_number: str, amount: float):
        pass

    def withdraw(self, account_number: str, amount: float):
        pass

    def transfer_funds(self, from_acc_num: str, to_acc_num: str, amount: float):
        pass

    def get_customer_accounts(self, customer_id: str):
        pass

    def display_all_customers(self):
        pass

    def display_all_accounts(self):
        pass

    def apply_all_interest(self):
        pass
