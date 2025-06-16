import json
import uuid

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
        def _load_data(self):
            try:
                with open(self.customer_file, 'r') as f:
                    try:
                        customers_data = json.load(f)
                    except json.JSONDecodeError:
                        customers_data = []

                for c in customers_data:
                    customer = Customer(
                        c['customer_id'],
                        c['name'],
                        c['address']
                    )
                    for acc_no in c.get('account_numbers', []):
                        customer.add_account_number(acc_no)
                    self._customers[customer.customer_id] = customer
            except FileNotFoundError:
                pass

            try:
                with open(self.account_file, 'r') as f:
                    try:
                        accounts_data = json.load(f)
                    except json.JSONDecodeError:
                        accounts_data = []

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
                        continue
                    self._accounts[account.account_number] = account
            except FileNotFoundError:
                pass

    def _save_data(self):
        with open(self.customer_file, 'w') as f:
            json.dump([cust.dict_details() for cust in self._customers.values()], f,indent = 4)

        with open(self.account_file, 'w') as f:
            json.dump([acc.display_details() for acc in self._accounts.values()], f,indent = 4)


    def AddCustomer(self, customer):
        if customer.customer_id in self._customers :
            return False
        self._customers[customer.customer_id] = customer
        self._save_data()
        return True
    def RemoveCustomer(self, customer_id):
        customer = self._customers.get(customer_id)
        if not customer :
            return False
        if customer._account_numbers:
            return False
        del self._customers[customer_id]
        self._save_data()
        return True

    def create_account(self, customer_id: str, account_type: str, initial_balance = 0.0, **kwargs):
        if customer_id not in self._customers:
            return None

        account_number = str(uuid.uuid4())
        if account_type.lower() =="savings" :
            account = SavingsAccount(
                account_number,
                customer_id,
                initial_balance,
                kwargs.get("interest_rate", 0.01)
            )
        elif account_type.lower() == "checking":
            account = CheckingAccount(
                account_number,
                customer_id,
                initial_balance,
                kwargs.get("overdraft_limit", 0.0)
            )
        else :
            return None

        self._accounts[account_number] =account
        self._customers[customer_id].add_account_number(account_number)
        self._save_data()
        return account
    def deposit(self, account_number, amount):
        account = self._accounts.get(account_number)
        if account and account.deposit(amount):
            self._save_data()
            return True
        return False
    def withdraw(self, account_number, amount):
        account = self._accounts.get(account_number)
        if account and account.withdraw(amount):
            self._save_data()
            return True
        return False

    def transfer_funds(self, from_acc_num, to_acc_num, amount):
        from_account = self._accounts.get(from_acc_num)
        to_account = self._accounts.get(to_acc_num)
        if not from_account or not to_account:
            return False
        if from_account.withdraw(amount) and to_account.deposit(amount):
            self._save_data()
            return True
        return False

    def get_customer_accounts(self, customer_id):
        customer = self._customers.get(customer_id)
        if not customer:
            return []
        return [self._accounts[acc_no] for acc_no in customer.account_numbers if acc_no in self._accounts]


    def display_all_customers(self):
        for customer in self._customers.values():
            customer.display_details()

    def display_all_accounts(self):
        for account in self._accounts.values():
            account.display_details()


    def apply_all_interest(self):
        for account in self._accounts.values():
            if isinstance(account, SavingsAccount):
                account.apply_interest()
            self._save_data()
