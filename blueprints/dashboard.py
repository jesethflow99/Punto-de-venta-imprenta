from flask import Blueprint,redirect,render_template,url_for

dashboard = Blueprint('dashboard',__name__)

@dashboard.route('/')
def index():
    return render_template('dashboard/dashboard.html',name='Edgar',role='Administrador')


@dashboard.route('/ventas')
def puntoVenta():
    return render_template('dashboard/ventas.html',name='Edgar',role='Administrador')

@dashboard.route('/clientes')
def clientes():
    return render_template('dashboard/clientes.html',name='Edgar',role='Administrador')

@dashboard.route('/inventarios')
def inventarios():
    return render_template('dashboard/inventarios.html',name='Edgar',role='Administrador')


@dashboard.route('/facturas')
def facturas():
    return render_template('dashboard/facturas.html',name='Edgar',role='Administrador')

@dashboard.route('/reportes')
def reportes():
    return render_template('dashboard/reportes.html',name='Edgar',role='Administrador')

@dashboard.route('/configuracion')
def configuracion():
    return render_template('dashboard/configuracion.html',name='Edgar',role='Administrador')