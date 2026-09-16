from sqlalchemy.orm import Session
from app.models.account import Account
from app.models.transaction import Transaction

def create_account(db: Session, user_id: int, account_type: str):
    new_account = Account(user_id=user_id, account_type=account_type, balance=0)
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return new_account

def get_account(db: Session, account_id: int):
    account = db.query(Account).filter(Account.account_id == account_id).first()
    if account is None:
        raise ValueError("Account does not exist")
    else:
        return account

def deposit(db: Session, account_id: int, amount: float):
    if amount <= 0:
        raise ValueError("Amount must be a positive number")
    account = get_account(db, account_id)
    account.balance += amount
    new_transaction = Transaction(account_id=account_id, amount = amount, txn_type = "DEPOSIT")
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction


def withdraw(db: Session, account_id: int, amount: float):
    if amount <= 0:
        raise ValueError("Amount must be a positive number")
    account = get_account(db, account_id)
    if amount > account.balance:
        raise ValueError("Cannot withdraw more than current balance")
    account.balance -= amount
    new_transaction = Transaction(account_id=account_id, amount = amount, txn_type = "WITHDRAW")
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction

def get_transactions(db: Session, account_id: int):
    account = get_account(db, account_id)
    return db.query(Transaction).filter(Transaction.account_id == account_id).all() 


