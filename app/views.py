from flask import render_template, redirect, jsonify, flash, request, url_for
from app import app
from app.forms import LoginForm
import json

user = {}

@app.route('/', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if  form.validate_on_submit():
        flash('Login requests for users {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        if form.username.data not in user:
            user[form.username.data] = 1
        return redirect(url_for('game'))
    return render_template('login.html', form=form)


@app.route('/game', methods=['POST', 'GET'])
def game():
    data = request.form
    value_from_js = data.get('key1', None)

    print(value_from_js)
    return render_template('index.html')


