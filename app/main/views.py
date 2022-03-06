from flask import render_template,request,redirect,url_for
from flask import render_template
from app import app
from ..models import User,Pitch
from flask_login import login_required

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    all_pitches=Pitch.query.order_by('id').all()
    print(all_pitches)
    title='Pitch App'
    return render_template('index.html',title=title)
    