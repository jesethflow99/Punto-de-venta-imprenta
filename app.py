from flask import Flask, redirect, url_for,render_template
from blueprints.auth import auth
from blueprints.dashboard import dashboard
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(auth, url_prefix='/auth')  # Asegúrate del slash inicial
app.register_blueprint(dashboard,url_prefix='/dashboard')

@app.route('/')
def index():
    return redirect(url_for('auth.login'))


@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template("404.html"), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000,host='0.0.0.0')
