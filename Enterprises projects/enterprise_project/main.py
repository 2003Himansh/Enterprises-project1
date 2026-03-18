import logging
from datetime import datetime
from typing import List, Dict, Any

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

import uvicorn

from database import get_db, SessionLocal, engine, Base
from models import User
from schemas import ProductCreate, OrderCreate
from services import ProductService, OrderService, UserService
from middleware import LoggingMiddleware, RateLimitMiddleware
from config import settings

# Create tables
Base.metadata.create_all(bind=engine)

# Logging
logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.FileHandler("logs/app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Enterprise E-Commerce Platform",
    version="1.0.0"
)

# Middleware
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_methods=["*"],
                   allow_headers=["*"])

app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])
app.add_middleware(LoggingMiddleware)
app.add_middleware(RateLimitMiddleware)

# Security
security = HTTPBearer()


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    user_service = UserService()

    user = user_service.verify_token(token)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid Token")

    return user


# Health API
@app.get("/health")
def health():
    return {
        "status": "OK",
        "time": datetime.utcnow()
    }


# Products
@app.get("/products", response_model=List[Dict[str, Any]])
def get_products(db=Depends(get_db)):
    return ProductService(db).get_products()


@app.post("/products")
def create_product(product: ProductCreate,
                   db=Depends(get_db),
                   user=Depends(get_current_user)):
    return ProductService(db).create_product(product, user["id"])


# Orders
@app.post("/orders")
def create_order(order: OrderCreate,
                 db=Depends(get_db),
                 user=Depends(get_current_user)):

    return OrderService(db).create_order(order, user["id"])


if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.HOST, port=settings.PORT, reload=True)