import os
import json

# Ruta del archivo de configuración
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "../config_files/negocio.json")

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
        print("⚠️ Configuración no encontrada, creando archivo por defecto.")
        set_dataConfig(DEFAULT_CONFIG)
        return DEFAULT_CONFIG

    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
        print("📦 Configuración actual:")
        print(json.dumps(data, indent=4, ensure_ascii=False))
        return data

# Test rápido
#if __name__ == "__main__":
#   config = get_dataConfig()

    # Puedes editarlo aquí si quieres hacer pruebas
    # config["name"] = "Nuevo nombre"
    # set_dataConfig(config)
