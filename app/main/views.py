from flask import render_template,request,redirect,url_for
from .forms import PitchForm,CommentForm, UpdateProfile
from app import app
from . import main
from ..models import User,Pitch
from flask_login import login_required,current_user

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

@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        category = form.category.data
        newPitch = form.pitch_info.data
        #update pitch instance
        new_pitch = Pitch(pitch_title=title,
                          pitch_category=category,
                          pitch_itself=newPitch,
                          user=current_user)
        #save pitch
        new_pitch.save_pitch()
        return redirect(url_for('.index'))
    title = 'Add New pitch'
    return render_template('pitches.html', title=title, pitchesform=form) 


@main.route('/category/tech')
def tech():
    '''
    view function to display sports pitches
    '''
    pitches=Pitch.get_pitches('tech')
    tech_title ='tech Pitches'
    return render_template('pitches/tech.html',title=tech_title,tech_pitch=pitches)


@main.route('/category/sciences')
def sciences():
    '''
    view function to display business pitches
    '''
    pitches=Pitch.get_pitches('sciences')
    sciences_title='sciences Pitches'
    return render_template('pitches/business.html',title=sciences_title, sciences_pitch=pitches)       
    