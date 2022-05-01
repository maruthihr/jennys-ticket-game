import flask
import requests
import json
from flask import request, jsonify, render_template, g

app = flask.Flask(__name__) # creating an instance of the Flask class

  
 
@app.route('/') # The primary url for our application
def index(): 
    return render_template("rdm6easy.html")

 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port= 8080) 
