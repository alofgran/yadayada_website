from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    #Fake data for setup only --> will pull from database later
    user = {'username': 'Alex'}
    posts = [
        {
            'title': 'My kid has a fever',
            'description': 'Discussing fevers in pediatric patients',
            'filename': 'health_pediatrics_fever.mov'
        },
        {
            'title': 'Everything you wanted to know about UTIs',
            'description': 'Urinary Tract Infections',
            'filename': 'health_family_uti.mov'
        },
        {
            'title': 'Reducing personal debt',
            'description': 'Learn how to eliminate your debt',
            'filename': 'finance_debt.mov'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit(): #gathers data, runs validators, and submits if all good (True)
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
