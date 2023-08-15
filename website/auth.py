from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db 

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", boolean=False)

@auth.route('/logout')
def logout():
    return "<p>LOGOUT</p>"

@auth.route('/signUp', methods=['GET', 'POST'])
def sign_up():
    if request.method== 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email not valid', category='error')
        elif len(first_name) <2:
            flash('Invalid Name', category='error')
        elif password1!=password2:
            flash('Different Passwords', category='error')
        elif len(password1) < 8:
            flash('Password must be atleast 8 charachters', category='error')
        else:
            new_user = User(email=email,first_name=first_name,password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()

            flash("Account Created Successfully", category="success")
            return redirect(url_for('view.home'))

    return render_template("sign_up.html")