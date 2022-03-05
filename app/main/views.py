from flask import render_template,request,redirect,url_for
from flask import render_template
from app import app
from ..models import User,Pitch

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')