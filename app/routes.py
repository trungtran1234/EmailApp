from sqlalchemy import or_
from app import db
from glob import escape
from flask import flash, redirect, render_template, url_for
from flask_login import LoginManager, current_user, login_required, login_user, logout_user

from app.models import User
from .forms import LoginForm, RegisterForm
from app import myapp_obj



@myapp_obj.route("/")
@myapp_obj.route("/index.html")
def index():
    return render_template('base.html')

@myapp_obj.route("/hello")
def hello():
    return "Hello World!"

@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = None
    
    if form.validate_on_submit():
        print(f'username: {form.username.data} and password: {form.password.data}')
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if user.check_password(form.password.data):
                login_user(user)
                return redirect(url_for('mainpage'))
            else:
                error = 'Invalid username or password. Please try again.'
        else: 
            error = 'Invalid username or password. Please try again.'
    return render_template('login.html', form=form, error=error)

@myapp_obj.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    error = None
    if form.validate_on_submit():
        existing_user = User.query.filter(or_(User.username==form.username.data, User.email==form.email.data)).first()
        if existing_user:
            if existing_user.username == form.username.data and existing_user.email != form.email.data:
                error = 'This username is already taken. Please choose a different one.'
            if existing_user.email == form.email.data and existing_user.username != form.username.data:
                error = 'This email is already taken. Please choose a different one.'
            if existing_user.email == form.email.data and existing_user.username == form.username.data:
                error = 'This username and email is already taken. Please choose a different ones.'
            return render_template('register.html', form=form, error=error)
        new_account = User(username=form.username.data, email = form.email.data)
        new_account.set_password(form.password.data)
        db.session.add(new_account)
        db.session.commit()
        return render_template('registered.html', name=new_account.username)
    return render_template('register.html', form=form)

@myapp_obj.route("/mainpage", methods=['GET', 'POST'])
@login_required
def mainpage():
    return render_template('mainpage.html')

@myapp_obj.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@myapp_obj.route("/settings")
@login_required
def settings():
    return render_template('settings.html')

@myapp_obj.route("/delete", methods=['POST'])
@login_required
def delete():
    db.session.delete(current_user)
    db.session.commit()
    logout_user()
    return redirect(url_for('index'))

