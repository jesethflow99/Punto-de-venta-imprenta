from flask_marshmallow import Marshmallow
from marshmallow import fields, validate

ma = Marshmallow()

class UserSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True) 
    password = fields.Str(load_only=True, allow_none=True)
    role = fields.Str(validate=validate.OneOf(["admin", "user"]), load_default="user")
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class ClientSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(allow_none=True)
    phone = fields.Str(allow_none=True)
    address = fields.Str(allow_none=True)
    active = fields.Bool(load_default=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class ProductCategorySchema(ma.Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class ProductSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    stock = fields.Int(required=True)
    unit_type = fields.Str(required=True)
    category_id = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class OrderSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    client_id = fields.Int(required=True)
    user_id = fields.Int(required=True)
    total = fields.Float(required=True)
    status = fields.Str(load_default="pending")
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class OrderDetailSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    order_id = fields.Int(required=True)
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True)
    subtotal = fields.Float(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class CashRegisterSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    opened_at = fields.DateTime(required=True)
    closed_at = fields.DateTime(allow_none=True)
    initial_balance = fields.Float(allow_none=True)
    final_balance = fields.Float(allow_none=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class CashMovementSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    cash_register_id = fields.Int(required=True)
    type = fields.Str(required=True, validate=validate.OneOf(["income", "expense"]))
    amount = fields.Float(required=True)
    description = fields.Str(allow_none=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class ExpenseSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    cash_register_id = fields.Int(required=True)
    description = fields.Str(required=True)
    amount = fields.Float(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class LogSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    action = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class SystemConfigSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    key = fields.Str(required=True)
    value = fields.Str(allow_none=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
