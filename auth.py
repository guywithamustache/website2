"""module doctring"""
from datetime import datetime
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db 


auth = Blueprint('auth', __name__)


#login logout and sign up function
@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user: 
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
            else:
                flash('Incorrect Password, try again', category='error')
        else:
            flash('username does not exist', category='error')

    return render_template("login.html", datetime = str(datetime.now()))

@auth.route('/logout')
def logout():
    return render_template("logout.html", datetime = str(datetime.now()))

@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        SpecialSym=['@','_','!','#','$','%','^','&','*','<','>','?','~']
        if len(password) <12:
            flash('password must have at least 12 characters', category='error')
        elif not any(char.isdigit() for char in password):
            flash('password must have at least 1 digit', category='error')
        elif not any(char.isupper() for char in password):
            flash('password must have at least 1 uppercase letter', category='error')
        elif not any(char.islower() for char in password):
            flash('password must have at least 1 lowercase letter', category='error')
        elif not any(char in SpecialSym for char in password):
            flash('password must have at least 1 special character', category='error')
        elif password != password2:
            flash('passwords do not match', category='error')
        else:
            new_user=User(username=username, password=generate_password_hash(password, method = 'sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created', category='success')
            return redirect(url_for('views.home'))


    return render_template("sign-up.html", datetime = str(datetime.now()))

#calling html template
@auth.route('/musk')
def musk():
    return render_template("musk.html", datetime = str(datetime.now()))

@auth.route('/yosef')
def yosef():
    return render_template("yosef.html", datetime = str(datetime.now()))


