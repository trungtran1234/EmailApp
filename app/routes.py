from glob import escape
from flask import flash, redirect, render_template
from .forms import LoginForm
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
        flash(f'Here are the input {form.username.data} and {form.password.data}')
        return redirect('/')
    return render_template('login.html', form=form)

@myapp_obj.route("/members/<string:name>/")
def getMember(name):
    return escape(name)
