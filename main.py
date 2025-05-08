from flask import Flask
from flask import redirect, request, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


