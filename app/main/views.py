from os import path
from flask import render_template, request, redirect, url_for, abort, flash
from . import main
from ..models import User, Pitch, Comment, Upvote, Downvote
from .. import db,photos
from flask_login import login_required, current_user
from .forms import PitchForm, UpdateProfile, CommentForm

@main.route('/')
def main_page():
    '''this is my main page where a user will either login or register to access the site'''

    return redirect(url_for('auth.login'))

@main.route('/login')
def landing_page():
    title = 'Mathwiti | Login'
    return render_template('index.html', title = title)

@main.route('/profile')
@login_required
def profile_page():
    title = 'Mathwiti | Profile'
    return render_template('profile/profile.html', title = title)

@main.route('/job')
@login_required
def job_page():
    title = 'Mathwiti | Job'
    pitch = Pitch.query.filter_by(category_of_the_pitch = 'Job').all()
    return render_template('job_page.html', title = title, pitch=pitch)

@main.route('/pitch/new', methods = ['GET','POST'])
@login_required
def new_pitch():
    title = 'Mathwiti | Create Pitch'
    job_new = PitchForm()
    if job_new.validate_on_submit():
        kichwa = job_new.title.data
        post = job_new.post.data
        category = job_new.category.data
        owner_id = current_user
        new_job = Pitch(user_id=current_user._get_current_object().id,pitch=post,category_of_the_pitch=category)
        new_job.save_pitch()
        #db.session.add(new_job)
        #db.session.commit()
        return redirect(url_for('main.profile_page'))
    return render_template('newPitch.html', title = title,job_new=job_new)

@main.route('/advert')
@login_required
def advert():
    title = "Mathwiti | Advertisements"
    pitch = Pitch.query.filter_by(category_of_the_pitch = 'Advertisement').all()
    return render_template("advertisment.html", title= title, pitch=pitch)

@main.route('/comment/new/<int:pitch_id>',methods = ["GET","POST"])
@login_required
def new_comment(pitch_id):
    title = "Mathwiti | Comment"
    form = CommentForm()
    if form.validate_on_submit():
        comment = form.comment.data
        owner_id = current_user
        comment_mpya = Comment(user_id=current_user._get_current_object().id,comment=comment, post_id = pitch_id)
        db.session.add(comment_mpya)
        db.session.commit()
        return redirect(url_for('main.profile_page'))
    return render_template('comment.html',title=title,comment_form=form)

@main.route('/user/chicken/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    title = current_user.username + " | Pitch"
    if user is None:
        abort(404)
        
    return render_template("profile/user_profile.html", user = user, title = title)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname = user.username))

    return render_template('profile/update.html',form=form)

@main.route('/user/<uname>/update/pic',methods = ['POST'])
@login_required
def update_picha(uname):
    user = User.query.filter_by(username = uname).first()
    print(request.files)
    if 'pichaYako' in request.files:
        print("hi")
        filename = photos.save(request.files['pichaYako'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()

    return redirect(url_for('main.profile',uname = uname))