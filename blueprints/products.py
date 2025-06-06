from flask import Blueprint,redirect,url_for,request,flash
from models import db, Product,ProductCategory

products = Blueprint("products",__name__)

@products.route("/",methods=["POST"])
def product_reg():
  if request.method == "POST":
    name = request.form.get("name")
    price = request.form.get("price")
    stock = request.form.get("stock")
    unyt_type = request.form.get("unyt_type")
    category_id = request.form.get()
    product = Product(name,price,stock,unyt_type,category_id)
    db.session.add(product)
    db.session.commit()
    return redirect(url_for("dashboard.configuracion"))

@products.route("/<int:id>",methods=["POST","GET"])
def product(id):
  if request.method == "POST":
    product = db.session.get(Product,id)
    if product:
      product.name = request.form.get("name",product.name)
      product.price = request.form.get("price",product.price)
      product.stock = request.form.get("stock",product.stock)
      product.unyt_type = request.form.get("unyt_type",product.unit_type)
      product.category_id = request.form.get("category_id",product.category_id)
      db.session.commit()
      flash("Producto agregado con Exito","success")
    else:
      flash("No se pudo agregar el producto","danger")
    return redirect(url_for("dashboard.configuracion"))
  
@products.route("/category",methods=["POST"])
def category():
  if request.method =="POST":
    try:
      name = request.form.get("name")
      print(name)
      category = ProductCategory(name=name)
      print(category)
      db.session.add(category)
      db.session.commit()
      flash("Categoria agregada con exito","success")
    except:
      flash("No se pudo agregar la categoria ","danger")  
  return redirect(url_for("dashboard.configuracion"))
