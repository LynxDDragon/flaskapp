from . import bp as app
from flask import render_template

@app.route('/blog')
def Blog():
    return render_template('blog.html')