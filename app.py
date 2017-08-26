from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Flask'

@app.route('/about')
def about():
    return 'This page is for learning purpose'

@app.route('/greeting/')
@app.route('/greeting/<name>')
def greeting(name=None):
    return render_template('greeting.html', name=name)

@app.route('/post/<int:post_id>')
def show_port(post_id):
    # show the post with the given id, the id is an integer
    return 'Post {}'.format(post_id)
