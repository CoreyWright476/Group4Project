from flask import render_template

from application import app

@app.route('/')
@app.route('/login')
def login():
    return render_template('login.html', title='Please sign in')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/recipies')
def recipies():
    return render_template('recipies.html')

@app.route('/test')
def test():
    return 'test'