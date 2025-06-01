from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ModelBase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

class Usuario(ModelBase):
    __tablename__ = 'usuarios'
    
    nombre = db.Column(db.String(50), nullable=False)
    correo = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    rol = db.Column(db.String(20), nullable=False, default='cliente')  # cliente, admin, etc.
    
    phone = db.Column(db.String(50))
    address = db.Column(db.String(50))

