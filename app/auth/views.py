from flask import render_template,redirect,url_for,flash,request
from flask_login import login_user,logout_user,login_required
from ..models import User
from . import auth
from .forms import LoginForm, RegistrationForm
from .. import db
# from ..email import mail_message

@auth.route('/login')
def login():
    return render_template('auth/login.html')