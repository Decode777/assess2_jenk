from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Vaishnavi here!"

@app.route('/about')
def about():
    return "About Page"