from flask import Blueprint, render_template, redirect,url_for,flash,request

auth = Blueprint('auth',__name__)

@auth.route('/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        email = request.form.get('email')
        return redirect(url_for('dashboard.index'))
    