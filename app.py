from __future__ import with_statement
import os
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

DEBUG = True
SECRET_KEY = 'development key'

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('base.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0',port=port)
