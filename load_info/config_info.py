import os
import json
from models import db,User,Product,ProductCategory
import win32print

# Ruta del archivo de configuración
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "../config_files/negocio.json")

PRINTERS_PATH = os.path.join(os.path.dirname(__file__), "../config_files/printers.json")

# Configuración por defecto
DEFAULT_CONFIG = {
    "name": "Imprenta POS",
    "phone": "No establecido",
    "email": "No establecido",
    "address": "No establecido",
    "RUC": "No establecido"
}



def set_dataConfig(data):
    # Carga la configuración actual o usa la configuración por defecto
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            current_config = json.load(f)
    else:
        current_config = DEFAULT_CONFIG.copy()

    # Actualiza solo las claves presentes en data
    for key, value in data.items():
        if value:  # Ignora valores vacíos o None para no sobrescribir con basura
            current_config[key] = value

    os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(current_config, f, indent=4, ensure_ascii=False)
    print(f"✅ Configuración guardada en {CONFIG_PATH}")

# Carga los datos desde el JSON
def get_dataConfig():
    if not os.path.exists(CONFIG_PATH):
        set_dataConfig(DEFAULT_CONFIG)
        return DEFAULT_CONFIG

    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data
    
def list_printers():
    impresoras = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS)
    return [impresora[2] for impresora in impresoras]    

def config_printers():
    with open(PRINTERS_PATH, "r", encoding="utf-8") as f:
            config_printers = json.load(f)
    return config_printers

def load_data():
    data = {
        "users":User.query.all(),
        "categories":ProductCategory.query.all(),
        "products":Product.query.all(),
        "printers":list_printers(),
        "config_printers": config_printers()
    }   
    return data



