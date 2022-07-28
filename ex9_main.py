
#importing modules
from flask import Flask, request, jsonify
from flask_cors import CORS

#creating the APP itself
app = Flask(__name__)
 
#disabling CORS block for ALL sources
CORS(app)

#Creating the BL classes + importing the files
from BL.usersBL import *
usersBL = usersBL()


#/users Router - GET all users:
@app.route('/users', methods=['GET'])
def get_all():
    return jsonify(usersBL.get_all())

#/users Router - POST request:
@app.route('/users', methods=['POST'])
def post_user():
    usersBL.post_user(request.json)
    return jsonify(f"OK. I've added {request.json}")

#running the app 
app.run()