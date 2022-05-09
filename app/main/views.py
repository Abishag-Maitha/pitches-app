from crypt import methods
from flask_login import login_required
from flask import render_template,request,redirect,url_for,abort
from app import main
from ..models import User,Pitch,Comment,Upvote,Downvote
from .forms import UpdateProfile
from .. import db #photos

@main.route('/', methods=['GET','POST'])
def index():
    title='Pitches-App'
    all_pitches=Pitch.query.all()
    career_pitch=Pitch.query.filter_by(category="career").all()
    interview_pitch=Pitch.query.filter_by(category="career").all()

    return render_template("index.html",pitches=all_pitches,career=career_pitch, interview=interview_pitch)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user)

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

        return redirect(url_for('.profile',uname=user.username))
    return render_template('profile/update.html',form =form)

    
# @main.route('/user/<uname>/update/pic',methods= ['POST'])
# @login_required
# def update_pic(uname):
#     user = User.query.filter_by(username = uname).first()
#     if 'photo' in request.files:
#         filename = photos.save(request.files['photo'])
#         path = f'photos/{filename}'
#         user.profile_pic_path = path
#         db.session.commit()
#     return redirect(url_for('main.profile',uname=uname))