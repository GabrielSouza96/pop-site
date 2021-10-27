import flask
from flask import render_template, redirect, url_for, flash, request, send_file
from popsenfermagem import app
from werkzeug.utils import secure_filename
import os
import urllib.request
from pathlib import Path


@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('home.html')




