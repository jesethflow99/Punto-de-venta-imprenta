from flask import Blueprint, request, redirect, url_for, jsonify,flash
from models import db, User

users = Blueprint("users", __name__)

# --- GET ALL & CREATE ---
@users.route("/", methods=["GET", "POST"])
def users_table():
    if request.method == "GET":
        data = User.query.all()
        return jsonify([u.to_dict() for u in data])
    if request.method == "POST":
        try:
            name = request.form.get("name")
            email = request.form.get("email")
            password = request.form.get("password")
            role = request.form.get("role")
            flash("Usuario agregado por exito","success")
            user = User(name=name, email=email, password=password, role=role)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("dashboard.configuracion"))
        except:
            flash("No se pudo agregar el usuario","danger")
        
        return redirect(url_for("dashboard.configuracion"))


# --- UPDATE por ID ---
@users.route("/update/<int:user_id>", methods=["POST"])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404

    user.name = request.form.get("name", user.name)
    user.email = request.form.get("email", user.email)
    user.password = request.form.get("password", user.password)
    user.role = request.form.get("role", user.role)

    db.session.commit()
    return redirect(url_for("dashboard.configuracion"))


# --- DELETE por ID ---
@users.route("/delete/<int:user_id>", methods=["GET"])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        flash("error: Usuario no encontrado","danger")
        return redirect(url_for("dashboard.configuracion"))

    db.session.delete(user)
    db.session.commit()
    flash("Usuario eliminado con exito","success")
    return redirect(url_for("dashboard.configuracion"))
