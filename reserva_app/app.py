from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def principal():
    return render_template('principal.html')
