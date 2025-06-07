from flask import Blueprint,redirect,url_for,request,flash
from models import db, Product,ProductCategory
from schemas import ProductCategorySchema,ProductSchema
from marshmallow import ValidationError
products = Blueprint("products",__name__)

@products.route("/",methods=["POST"])
def product_reg():
  if request.method == "POST":
    try:
      if ProductCategory.query.all():
        product_schema = ProductSchema()
        data = product_schema.load(request.form.to_dict())
        product = Product(**data)
        db.session.add(product)
        db.session.commit()
        flash("Producto agregado satisfactoriamente","success")
        return redirect(url_for("dashboard.configuracion"))
      else:
        flash("No tienes categorias agregadas","warning")
        return redirect(url_for("dashboard.configuracion"))
    except ValidationError as err:
      flash(f"Error de validacion: {err}")
      return redirect(url_for("dashboard.configuracion"))
    except Exception as e:
      flash("No se pudo agregar el producto","danger")
      print(e)
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
  elif request.method == "GET":
    product = db.session.get(Product, id)
    if product:
        db.session.delete(product)
        db.session.commit()
        flash("Producto eliminado satisfactoriamente", "success")
    else:
        flash("El producto no existe o ya fue eliminado", "warning")
    return redirect(url_for("dashboard.configuracion"))

@products.route("/category",methods=["POST"])
def category():
  if request.method =="POST":
    try:
      category_schema = ProductCategorySchema()
      data = category_schema.load(request.form.to_dict())
      category = ProductCategory(**data)
      db.session.add(category)
      db.session.commit()
      flash("Categoria agregada con exito","success")
    except ValidationError as err:
      flash("Error de Validacion: "+err)
    except Exception as e:
      print(e)
      flash("No se pudo agregar la categoria ","danger")  
  return redirect(url_for("dashboard.configuracion"))

@products.route("/category/<int:id>", methods=["GET"])
def delete_category(id):
    try:
        productos_en_categoria = Product.query.filter_by(category_id=id).first()
        if productos_en_categoria:
            flash("No se pudo eliminar la categoría: contiene productos.", "danger")
        else:
            category = db.session.get(ProductCategory, id)
            if category:
                db.session.delete(category)
                db.session.commit()
                flash("Categoría eliminada con éxito.", "success")
            else:
                flash("Categoría no encontrada.", "warning")
    except Exception as e:
        print(f"[ERROR]: {e}")
        flash("Ocurrió un error al eliminar la categoría.", "danger")
    return redirect(url_for("dashboard.configuracion"))
