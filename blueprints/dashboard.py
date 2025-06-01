from flask import Blueprint,redirect,render_template,url_for

dashboard = Blueprint('dashboard',__name__)

@dashboard.route('/')
def index():
    return render_template('dashboard/dashboard.html',name='Edgar',role='Administrador')


@dashboard.route('/ventas')
def puntoVenta():
    return render_template('dashboard/ventas.html')

@dashboard.route('/clientes')
def clientes():
    return render_template('dashboard/clientes.html')