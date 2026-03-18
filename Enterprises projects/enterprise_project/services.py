from models import Product, Order, User
from jose import jwt
from config import settings


class ProductService:

    def __init__(self, db):
        self.db = db

    def get_products(self, skip=0, limit=100):
        return self.db.query(Product).offset(skip).limit(limit).all()

    def create_product(self, product, user_id):
        new_product = Product(**product.dict())
        self.db.add(new_product)
        self.db.commit()
        self.db.refresh(new_product)
        return new_product


class OrderService:

    def __init__(self, db):
        self.db = db

    def create_order(self, order, user_id):
        new_order = Order(
            product_id=order.product_id,
            user_id=user_id
        )
        self.db.add(new_order)
        self.db.commit()
        self.db.refresh(new_order)
        return {"id": new_order.id}


class UserService:

    def verify_token(self, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            return payload
        except:
            return None