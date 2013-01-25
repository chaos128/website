from __future__ import with_statement
import os

from flask import Flask, render_template

DEBUG = True
SECRET_KEY = 'development key'

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/team')
def team():
    return render_template('team.html')


@app.route('/jobs')
def jobs():
    return render_template('jobs.html')


@app.route('/press')
def press():
    return render_template('press.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
