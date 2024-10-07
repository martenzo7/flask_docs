from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello_world")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/")
def index():
    return render_template('index.html')
@app.route("/doc")
def doc():
    return render_template('doc.html')
