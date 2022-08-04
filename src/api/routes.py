"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, SThings
from api.utils import generate_sitemap, APIException
from dotenv import load_dotenv
load_dotenv()
import sendgrid
from sendgrid.helpers.mail import *
import os

api = Blueprint('api', __name__)

@api.route('/stranger_things', methods=['GET'])
def get_characters():
    people = SThings.query.all()
    characters=list(map(lambda x: x.serialize(), people))
    return jsonify(characters), 200


@api.route('/stranger_things', methods=['POST'])
def strthings():
    data = request.get_json()
    result = SThings(name=data["name"], gender=data["gender"], age=data["age"], alive=data["alive"], dob=data["dob"], description=data["description"])
    db.session.add(result)
    db.session.commit()
    return "Data Successfully Added"

@api.route('/stranger_things/<int:stranger_things_id>', methods=['DELETE'])
def delstrangerthings(stranger_things_id):
    sthings = SThings.query.get(stranger_things_id)
    if sthings is None:
        raise APIException(
            'This Character doesnt exist, or has already been deleted', status_code=404)
    delete_exotics = db.session.delete(sthings)
    db.session.commit()
    return jsonify(sthings.serialize())

@api.route('/resetpassword', methods=['POST'])
def reset():
    sg = sendgrid.SendGridAPIClient
    data = request.get_json()
    # user = User.query.filter_by(email=data['email']).first()
    # if user:
    to_email=To('nnngozi@gmail.com')
    subject = "New Title"
    email=data['email']
    mail=Mail(to_email, email, subject)
    response=sg.client.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)
    return 'sucess'

@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

