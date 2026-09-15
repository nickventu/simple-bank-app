from fastapi import APIRouter, HTTPException
from app.services import account_service
from app.schemas.account import AccountCreate, AccountResponse, AccountDeposit, AccountWithdraw
from app.schemas.transaction import TransactionResponse

router = APIRouter()

@router.post("/accounts", response_model=AccountResponse)
def create_account(payload: AccountCreate):
    account = account_service.create_account(payload.userId, payload.accountType)
    return AccountResponse(accountId=account.account_id, userName="???", balance=account.balance)

@router.get("/accounts/{id}",  response_model=AccountResponse)
def get_account(id: int):
    try:
        account = account_service.get_account(id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return AccountResponse(accountId=account.account_id, userName="???", balance=account.balance)

@router.post("/accounts/{id}/deposit", response_model=AccountResponse)
def deposit(id: int, payload: AccountDeposit):
    try:
        account_service.deposit(id, payload.amount)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    account = account_service.get_account(id)
    return AccountResponse(accountId=account.account_id, userName="???", balance=account.balance)

@router.post("/accounts/{id}/withdraw", response_model=AccountResponse)
def withdraw(id: int, payload: AccountWithdraw):
    try:
        account_service.withdraw(id, payload.amount)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    account = account_service.get_account(id)
    return AccountResponse(accountId=account.account_id, userName="???", balance=account.balance)

@router.get("/accounts/{id}/transactions", response_model=list[TransactionResponse])
def get_transactions(id: int):
    try:
        transactions = account_service.get_transactions(id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return [TransactionResponse(type=t.type, amount=t.amount, transaction_date=t.date) for t in transactions]