# -*- coding: utf-8 -*-

from scripts import tabledef
from scripts import forms
from scripts import helpers
from flask import Flask, redirect, url_for, render_template, request, session
import json
import sys
import os


app = Flask(__name__)


# ======== Routing =========================================================== #
@app.route('/', methods=['GET', 'POST'])

# -------- Signup ---------------------------------------------------------- #
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = forms.LoginForm(request.form)
    if request.method == 'POST':
        query = request.form['username'].lower()
        print(form.validate())
        if query:
            if helpers.get_natural_language_query(query):
                disc_result=helpers.get_natural_language_query(query)
                return json.dumps({'status': disc_result[0]+" score: "+ str(disc_result[1])+ "ID: "+disc_result[2]})
            return json.dumps({'status': 'no result found'})
        return json.dumps({'status': 'query required'})
    return render_template('login.html', form=form)


# ======== Main ============================================================== #

if __name__ == "__main__":
    app.secret_key = os.urandom(12)  # Generic key for dev purposes only
    app.run(debug=True, use_reloader=True)

