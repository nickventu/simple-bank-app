from fastapi import FastAPI
from app.database import Base, engine
from app.routers.accounts import router as accounts_router
from app.routers.users import router as users_router
from app.models import user, account, transaction

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(accounts_router, prefix="/api")
app.include_router(users_router, prefix="/api")
