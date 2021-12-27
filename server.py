############------------ IMPORTS ------------############
from flask import Flask


############------------ GLOBAL VARIABLE(S) ------------############
app = Flask(__name__)

############------------ FUNCTION(S) ------------############
@app.route("/")
def hello_world():
    return "<p>Hello World</p>"

############------------ DRIVER CODE ------------############
