#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal
db.init_app(app)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

# app/app.py

# ... (previous code)

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.filter(Animal.id == id).first()

    if not animal:
        response_body = '<h1>404 animal not found</h1>'
        response = make_response(response_body, 404)
        return response

    response_body = f'''
        <h1>Animal ID {animal.id}</h1>
        <ul>
            <li>Name: {animal.name}</li>
            <li>Species: {animal.species}</li>
            <li>Zookeeper: {animal.zookeeper.name}</li>
            <li>Enclosure: {animal.enclosure.environment}</li>
        </ul>
    '''

    response = make_response(response_body, 200)
    return response

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.filter(Zookeeper.id == id).first()

    if not zookeeper:
        response_body = '<h1>404 zookeeper not found</h1>'
        response = make_response(response_body, 404)
        return response

    response_body = f'''
        <h1>Zookeeper ID {zookeeper.id}</h1>
        <ul>
            <li>Name: {zookeeper.name}</li>
            <li>Birthday: {zookeeper.birthday}</li>
            <li>Animals: {len(zookeeper.animals)}</li>
        </ul>
    '''

    response = make_response(response_body, 200)
    return response

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.filter(Enclosure.id == id).first()

    if not enclosure:
        response_body = '<h1>404 enclosure not found</h1>'
        response = make_response(response_body, 404)
        return response

    animal_list = ', '.join([animal.name for animal in enclosure.animals])
    open_status = "open to visitors" if enclosure.open_to_visitors else "not open to visitors"

    response_body = f'''
        <h1>Enclosure ID {enclosure.id}</h1>
        <ul>
            <li>Environment: {enclosure.environment}</li>
            <li>Status: {open_status}</li>
            <li>Animals: {animal_list}</li>
        </ul>
    '''

    response = make_response(response_body, 200)
    return response

# ... (remaining code)

