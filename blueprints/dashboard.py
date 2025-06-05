from flask import Blueprint,redirect,render_template,url_for
from load_info.config_info import load_data

dashboard = Blueprint('dashboard',__name__)

@dashboard.route('/')
def index():
    return render_template('dashboard/dashboard.html')


@dashboard.route('/ventas')
def puntoVenta():
    return render_template('dashboard/ventas.html')

@dashboard.route('/clientes')
def clientes():
    return render_template('dashboard/clientes.html')

@dashboard.route('/inventarios')
def inventarios():
    return render_template('dashboard/inventarios.html')


@dashboard.route('/facturas')
def facturas():
    return render_template('dashboard/facturas.html')

@dashboard.route('/reportes')
def reportes():
    return render_template('dashboard/reportes.html')

@dashboard.route('/configuracion')
def configuracion():
    return render_template('dashboard/configuracion.html',**load_data())