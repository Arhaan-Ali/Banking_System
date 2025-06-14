from abc import ABC, abstractmethod
class Account(ABC) :
    def __init__(self, _account_number, _account_holder_id, initial_balance = 0.0 ):
        self._account_number = _account_number
        self.initial_balance = initial_balance
        self._account_holder_id= _account_holder_id

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def display_details(self):
        print(f"Acc No: {self._account_number},Balance: ${self.initial_balance}")

    def to_dict(self):
        return {
        "account_number": self._account_number,
        "balance": self.initial_balance,
        "account_holder_id": self._account_holder_id
    }

class SavingsAccount(Account):
    def __init__(self, _account_number, _account_holder_id, initial_balance = 0.0, interest_rate = 0.01):
        super().__init__(_account_number, _account_holder_id, initial_balance)
        self._interest_rate = interest_rate

    def deposit(self, amount):
        if amount > 0 :
            self.initial_balance += amount
            return True
        return  False

    def withdraw(self, amount):
        if 0 < amount <= self.initial_balance:
            self.initial_balance -= amount
            return True
        return False



class CheckingAccount(Account):
    def __init__(self, _account_number, _account_holder_id, initial_balance = 0.0, overdraft_limits = 0.0):
        super().__init__(_account_number, _account_holder_id, initial_balance)
        self.overdraft_limit = overdraft_limits

    def deposit(self, amount):
        if amount > 0 :
            self.initial_balance += amount
            return True
        return  False

    def withdraw(self, amount):
        if 0 < amount and  (self.initial_balance - amount) >= self.overdraft_limit :
            self.initial_balance -= amount
            return True
        return False
