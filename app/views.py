


    	posts = posts)
    	title = 'Home',
    	user = user,
            'author': { 'nickname': 'John' },
            'author': { 'nickname': 'Susan' },
            'body': 'Beautiful day in Portland!'
            'body': 'The Avengers movie was so cool!'
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        form = form,
        providers = app.config['OPENID_PROVIDERS'])
        return redirect('/index')
        title = 'Sign In',
        {
        {
        }
        },
    ]
    form = LoginForm()
    if form.validate_on_submit():
    posts = [
    return render_template("index.html",
    return render_template('login.html',
    user = { 'nickname': 'Miguel' }
@app.route('/')
@app.route('/index')
@app.route('/login', methods = ['GET', 'POST'])
def index():
def login():
from app import app
from flask import render_template, flash, redirect
from forms import LoginForm