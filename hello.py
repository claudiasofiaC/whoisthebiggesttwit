""" Minimal flask app"""

from flask import Flask

# make the application
app = Flask(__name__)

# make the route
@app.route("/")

# define a function
def hello():
    return "Hello World!"

# make a second route
@app.route("/about")

# now make the function that goes with about
def preds():
    return render_template('about.html')    
