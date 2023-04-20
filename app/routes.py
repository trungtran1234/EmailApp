from app import db
from glob import escape
from flask import flash, redirect, render_template, request, session, url_for
from flask_login import login_user

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

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if user.check_password(form.password.data):
                return redirect(url_for('index'))
        return '<h1>Invalid username or password</h1>'
    return render_template('login.html', form=form)

@myapp_obj.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        new_account = User(username=form.username.data, email = form.email.data)
        new_account.set_password(form.password.data)
        db.session.add(new_account)
        db.session.commit()
        return '<h1>Account created successfully</h1>'
    return render_template('register.html', form=form)

@myapp_obj.route("/members/<string:name>/")
def getMember(name):
    return escape(name)
