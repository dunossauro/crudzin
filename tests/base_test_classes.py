from base64 import b64encode
from unittest import TestCase
from flask import url_for
from app import create_app


def create_token(client, user):
    # return client.get(
    #     url_for('user.get_auth_token'),
    #     headers=headers
    # ).json['token']
    ...


class TestFlaskBase(TestCase):
    def setUp(self):
        """Roda antes de todos os testes."""
        self.app = create_app()
        self.app.testing = True
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.app.db.create_all()
        self.header = self.create_user()

    def tearDown(self):
        """Roda depois de todos os testes."""
        self.app.db.drop_all()


class TestFlaskLoged(TestFlaskBase):
    def setUp(self):
        TestFlaskBase.setUp(self)
        self.header = self.create_user()

    def tearDown(self):
        """Roda depois de todos os testes."""
        self.app.db.drop_all()

    def create_user(self):
        user = {
            'username': 'test',
            'password': '1234'
        }
        self.client.post(url_for('user.create_user'), json=user)
        return {
            'Authorization': 'Basic ' + b64encode(
                bytes(user['username'] + ":" + user['password'], 'ascii')
            ).decode('ascii')
        }
