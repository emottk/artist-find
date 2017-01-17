from flask import Flask
app = Flask(__name__)
from .. import spotify

@app.route('/')
def index():
    return "hello!"
