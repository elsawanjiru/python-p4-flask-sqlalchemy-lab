# app/models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    species = db.Column(db.String(255), nullable=False)
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeeper.id'), nullable=False)
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosure.id'), nullable=False)

class Zookeeper(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    animals = db.relationship('Animal', backref='zookeeper', lazy=True)

class Enclosure(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String(255), nullable=False)
    open_to_visitors = db.Column(db.Boolean, nullable=False)
    animals = db.relationship('Animal', backref='enclosure', lazy=True)
