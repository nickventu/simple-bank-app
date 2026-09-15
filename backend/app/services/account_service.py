from datetime import date
account_storage = {}
transaction_storage = {}

class Account():
    def __init__(self, account_id, user_id = 0, balance = 0, account_type = ""):
        self.account_id = account_id
        self.user_id = user_id
        self.balance = balance
        self.account_type = account_type

class Transaction():
    def __init__(self, account_id, txn_id, type = "", amount = 0.0, date = ""):
        self.account_id = account_id
        self.txn_id = txn_id
        self.type = type
        self.amount = amount
        self.date = date


def create_account(user_id, account_type):
    next_id = len(account_storage) + 1
    new_account = Account(user_id = user_id, account_type= account_type, account_id= next_id, balance = 0)
    account_storage[next_id] = new_account

    return new_account

def get_account(account_id):
    if account_id not in account_storage:
        raise ValueError("Account does not exist")
    return account_storage[account_id]

def deposit(account_id, amount):
    if amount <= 0:
        raise ValueError("Amount must be a positive number")
    account = get_account(account_id)
    account.balance += amount
    next_id = len(transaction_storage) + 1
    new_transaction = Transaction(account_id=account_id, txn_id= next_id,type = "DEPOSIT", amount = amount, date = date.today())
    transaction_storage[next_id] = new_transaction

    return new_transaction


def withdraw(account_id, amount):
    if amount <= 0:
        raise ValueError("Amount must be a positive number")
    account = get_account(account_id)
    if amount > account.balance:
        raise ValueError("Cannot withdraw more than current balance")
    account.balance -= amount
    next_id = len(transaction_storage) + 1
    new_transaction = Transaction(account_id=account_id, txn_id= next_id,type = "WITHDRAW", amount = amount, date = date.today())
    transaction_storage[next_id] = new_transaction

    return new_transaction

def get_transactions(account_id):
    get_account(account_id)
    return [txn for txn in transaction_storage.values() if txn.account_id == account_id]


