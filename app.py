from flask import Flask, redirect, url_for,render_template,request
from blueprints.auth import auth
from blueprints.dashboard import dashboard
from blueprints.users import users
from blueprints.products import products
from blueprints.config import config
from config import Config
from models import db
from load_info.config_info import get_dataConfig,set_dataConfig
from schemas import ma

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
ma.init_app(app)

app.register_blueprint(auth, url_prefix='/auth')  
app.register_blueprint(dashboard,url_prefix='/dashboard')
app.register_blueprint(users,url_prefix="/users")
app.register_blueprint(products,url_prefix="/products")
app.register_blueprint(config,url_prefix="/config")

ma.init_app
@app.context_processor
def inject_config():
    config = get_dataConfig()
    return dict(config_negocio=config)

from flask import request, redirect, url_for

@app.route("/saveConfig", methods=["POST"])
def SaveConfig():
    data = {
        "name": request.form.get("name", "").strip(),
        "RUC": request.form.get("RUC", "").strip(),
        "phone": request.form.get("phone", "").strip(),
        "email": request.form.get("email", "").strip(),
        "address": request.form.get("address", "").strip()
    }

    set_dataConfig(data)

    return redirect(url_for('dashboard.configuracion'))

    
    


@app.route('/')
def index():
    return redirect(url_for('auth.login'))


@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template("404.html"), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5000,host='0.0.0.0')
