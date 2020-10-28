from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Mark'}
    posts = [
        {
            'author': {'username': 'Mark'},
            'body': 'Beautiful day in Philippines!'
        },
        {
            'author': {'username': 'Karl'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
