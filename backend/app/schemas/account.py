from pydantic import BaseModel

class AccountCreate(BaseModel):
    userId: int
    accountType: str

class AccountResponse(BaseModel):
    accountId: int
    userName: str
    balance: float

class AccountDeposit(BaseModel):
    amount: float

class AccountWithdraw(BaseModel):
    amount: float