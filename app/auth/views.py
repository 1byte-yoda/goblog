from . import auth
from flask import render_template, request, redirect, url_for, flash, session
from . forms import LoginForm, RegistrationForm
from .. models import User
from flask_login import login_user, logout_user, login_required
from .. import db

@auth.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.verify_password(password=form.password.data):
            login_user(user, form.remember_me.data)
            session['name'] = user.username
            next = request.args.get('next')
            if next and next.startswith('/'):
                print('next')
                return redirect(next)
            else:
                print('main')
                return redirect(url_for('main.index', name=session.get('name')))
            flash('Invalid username or password')
    return render_template('auth/login.html', form=form)

@login_required
@auth.route('/logout')
def logout():
    logout_user()
    session['name'] = None
    flash("You've been logged out.")
    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    password=form.password.data,
                    email=form.email.data)
        db.session.add(user)
        db.session.commit()
        flash('You can now log in!')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)
