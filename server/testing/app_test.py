# server/testing/app_test.py

import pytest
from app import app, db  # Import your Flask app and database instance

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    client = app.test_client()

    with app.app_context():
        db.create_all()

    yield client

    with app.app_context():
        db.drop_all()

def test_example(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the pet/owner directory!' in response.data
