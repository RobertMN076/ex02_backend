#py -3 -m venv .venv
#.venv\Scripts\activate
# pip install flask
#python -m flask --app <arquivo> run --debug

from flask import Flask
from flask import redirect, request, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

usuarios = {
    'robert': '9099',
    'giulio': '8088',
}


