#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import url_for
from flask_httpauth import HTTPBasicAuth
from flask import g, session, redirect, url_for
from flask_simpleldap import LDAP
import json
import os

auth = HTTPBasicAuth()
app = Flask(__name__)
app.debug = True

@auth.get_password
def get_password(username):
    if username == 'toto':
        return 'python'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


try:
    student_age_file_path
    student_age_file_path  = os.environ['student_age_file_path']
except NameError:
    student_age_file_path  = '/data/student_age.json'

student_age_file = open(student_age_file_path, "r")
student_age = json.load(student_age_file)

@app.route('/pozos/api/v1.0/get_student_ages', methods=['GET'])
"student_age.py" 58L, 1667C

