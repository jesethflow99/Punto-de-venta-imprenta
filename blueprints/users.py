from flask import Blueprint,request,redirect,url_for
from models import db,User

users = Blueprint("users",__name__)

@users.route("/",methods=["POST","GET"])
def users_table():
    if request.method == "GET":
        data = User.query.all()
        print(data)
        return data 
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        role = request.form.get("role")