from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ModelBase(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    creado = db.Column(db.DateTime, server_default=db.func.now())
    actualizado = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

# ----------------- USUARIOS -----------------
class Rol(ModelBase):
    nombre = db.Column(db.String(50), nullable=False, unique=True)

class Usuario(ModelBase):
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    rol_id = db.Column(db.Integer, db.ForeignKey('rol.id'), nullable=False)
    rol = db.relationship('Rol')

# ----------------- CLIENTES -----------------
class Cliente(ModelBase):
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True)
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(255))
    activo = db.Column(db.Boolean, default=True)

# ----------------- PRODUCTOS -----------------
class CategoriaProducto(ModelBase):
    nombre = db.Column(db.String(100), nullable=False)

class Proveedor(ModelBase):
    nombre = db.Column(db.String(100), nullable=False)
    contacto = db.Column(db.String(100))

class Producto(ModelBase):
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria_producto.id'))
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedor.id'))

# ----------------- ORDENES -----------------
class Orden(ModelBase):
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    total = db.Column(db.Float, nullable=False)
    estado = db.Column(db.String(50), default='pendiente')

class DetalleOrden(ModelBase):
    orden_id = db.Column(db.Integer, db.ForeignKey('orden.id'))
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'))
    cantidad = db.Column(db.Integer, nullable=False)
    subtotal = db.Column(db.Float, nullable=False)

# ----------------- CAJA -----------------
class Caja(ModelBase):
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    apertura = db.Column(db.DateTime, nullable=False)
    cierre = db.Column(db.DateTime)
    saldo_inicial = db.Column(db.Float)
    saldo_final = db.Column(db.Float)

class MovimientoCaja(ModelBase):
    caja_id = db.Column(db.Integer, db.ForeignKey('caja.id'))
    tipo = db.Column(db.String(50))  # ingreso o egreso
    monto = db.Column(db.Float, nullable=False)
    descripcion = db.Column(db.String(255))

# ----------------- GASTOS -----------------
class Gasto(ModelBase):
    caja_id = db.Column(db.Integer, db.ForeignKey('caja.id'))
    descripcion = db.Column(db.String(255), nullable=False)
    monto = db.Column(db.Float, nullable=False)

# ----------------- CONTROL Y CONFIG -----------------
class Bitacora(ModelBase):
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    accion = db.Column(db.String(255), nullable=False)

class ConfiguracionSistema(ModelBase):
    clave = db.Column(db.String(50), unique=True, nullable=False)
    valor = db.Column(db.String(255))
