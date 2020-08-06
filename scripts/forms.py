# -*- coding: utf-8 -*-

from wtforms import Form, StringField, validators


class LoginForm(Form):
    query = StringField('username', validators=[validators.required(), validators.Length(min=1, max=250)])
