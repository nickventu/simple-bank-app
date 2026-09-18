from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services import account_service, user_service
from app.schemas.account import AccountCreate, AccountResponse, AccountDeposit, AccountWithdraw
from app.schemas.transaction import TransactionResponse
from app.services.auth_service import get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/accounts", response_model=AccountResponse)
def create_account(payload: AccountCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    account = account_service.create_account(db, current_user.user_id, payload.accountType)
    user = user_service.get_user(db, account.user_id)
    return AccountResponse(accountId=account.account_id, userName=user.name, balance=account.balance)

@router.get("/accounts/{id}",  response_model=AccountResponse)
def get_account(id: int, db : Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        account = account_service.get_account(db, id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e)) from e
    if account.user_id != current_user.user_id:
        raise HTTPException(status_code=403, detail="Not authorized to view this account")
    user = user_service.get_user(db, account.user_id)
    return AccountResponse(accountId=account.account_id, userName=user.name, balance=account.balance)

@router.post("/accounts/{id}/deposit", response_model=AccountResponse)
def deposit(id: int, payload: AccountDeposit, db : Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    account = account_service.get_account(db, id)
    if account.user_id != current_user.user_id:
        raise HTTPException(status_code=403, detail="Not authorized to deposit to this account")
    try:
        account_service.deposit(db, id, payload.amount)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    account = account_service.get_account(db, id)
    user = user_service.get_user(db, account.user_id)
    return AccountResponse(accountId=account.account_id, userName=user.name, balance=account.balance)

@router.post("/accounts/{id}/withdraw", response_model=AccountResponse)
def withdraw(id: int, payload: AccountWithdraw, db : Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    account = account_service.get_account(db, id)
    if account.user_id != current_user.user_id:
        raise HTTPException(status_code=403, detail="Not authorized to withdraw from this account")
    try:
        account_service.withdraw(db, id, payload.amount)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    account = account_service.get_account(db, id)
    user = user_service.get_user(db, account.user_id)
    return AccountResponse(accountId=account.account_id, userName=user.name, balance=account.balance)

@router.get("/accounts/{id}/transactions", response_model=list[TransactionResponse])
def get_transactions(id: int, db : Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    account = account_service.get_account(db, id)
    if account.user_id != current_user.user_id:
        raise HTTPException(status_code=403, detail="Not authorized to view this account's transactions")
    try:
        transactions = account_service.get_transactions(db, id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return [TransactionResponse(type=t.txn_type, amount=t.amount, transaction_date=t.created_at.date()) for t in
        transactions]
