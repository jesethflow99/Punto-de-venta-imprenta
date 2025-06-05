from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ModelBase(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    def to_dict(self):
        """Convierte los atributos del modelo en un diccionario."""
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

# ----------------- USERS -----------------
class Roles:
    ADMIN = "admin",
    USER = "user"

class User(ModelBase):
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=True)
    role = db.Column(db.String(5), default=Roles.USER, nullable=False)

# ----------------- CLIENTS -----------------
class Client(ModelBase):
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(255))
    active = db.Column(db.Boolean, default=True)

# ----------------- PRODUCTS -----------------
class ProductCategory(ModelBase):
    name = db.Column(db.String(100), nullable=False)

class Supplier(ModelBase):
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100))

class Product(ModelBase):
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)
    category_id = db.Column(db.Integer, db.ForeignKey('product_category.id'))
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'))

# ----------------- ORDERS -----------------
class Order(ModelBase):
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    total = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default='pending')

class OrderDetail(ModelBase):
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer, nullable=False)
    subtotal = db.Column(db.Float, nullable=False)

# ----------------- CASH REGISTER -----------------
class CashRegister(ModelBase):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    opened_at = db.Column(db.DateTime, nullable=False)
    closed_at = db.Column(db.DateTime)
    initial_balance = db.Column(db.Float)
    final_balance = db.Column(db.Float)

class CashMovement(ModelBase):
    cash_register_id = db.Column(db.Integer, db.ForeignKey('cash_register.id'))
    type = db.Column(db.String(50))  # income or expense
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255))

# ----------------- EXPENSES -----------------
class Expense(ModelBase):
    cash_register_id = db.Column(db.Integer, db.ForeignKey('cash_register.id'))
    description = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Float, nullable=False)

# ----------------- LOGGING AND CONFIG -----------------
class Log(ModelBase):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    action = db.Column(db.String(255), nullable=False)

class SystemConfig(ModelBase):
    key = db.Column(db.String(50), unique=True, nullable=False)
    value = db.Column(db.String(255))
