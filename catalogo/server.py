from flask import Flask, render_template, send_file, send_from_directory

app = Flask(__name__)

@app.route("/template")
def home():
    return render_template('index.html')

@app.route("/images/<file>")
def send_image(file):
    return send_from_directory('static/images', file)

@app.route("/")
def home2():
    return send_file('static/index.html')

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"