from flask import Blueprint, request, redirect, url_for,flash
import json
import os

config = Blueprint("config", __name__)

CONFIG_PATH = os.path.join("config_files", "printers.json")

@config.route("/printers", methods=["POST"])
def printers():
    data = request.form.to_dict()
    if not data:
        flash("Datos no recibidos","warning")
        return redirect(url_for("dashboard.configuracion"))
    os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    flash("Configuracion de impresoras establecido con exito","success")
    return redirect(url_for("dashboard.configuracion")) 

@config.route("/print/<str:printer>",methods = ["POST"])
def print(printer):
  data = request.method