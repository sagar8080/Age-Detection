import flask
from flask import request
app = flask(__name__)
@app.route('/')
def index(name="sagar"):
    return "hello from{}".format(name)

app.run(debug =True, port='8000' , host = '0.0.0.0')


