from flask import Flask, render_template

app = Flask(__name__)

@app.route('/jobs')
@app.route('/')
def jobs():
    """jobs route"""
    return render_template('index.html')