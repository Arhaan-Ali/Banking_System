from abc import ABC, abstractmethod
class Account(ABC) :
    def __init__(self, _account_number, _account_holder_id, initial_balance = 0.0 ):
        self._account_number = _account_number
        self.initial_balance = initial_balance
        self._account_holder_id= _account_holder_id

    def transactions(self):
        pass


class SavingsAccount(Account):
    def __init__(self, _account_number, _account_holder_id, initial_balance = 0.0, interest_rate = 0.01):
        super().__init__(_account_number, _account_holder_id, initial_balance)
        self._interest_rate = interest_rate

    def transactions(self):
        pass

class CheckingAccount(Account):
    def __init__(self, _account_number, _account_holder_id, initial_balance = 0.0, overdraft_limits = 0.0)
        super().__init__(_account_number, _account_holder_id, initial_balance)
        self.overdraft_limit = overdraft_limits

    def transactions(self):
        pass
