from flask import url_for
from flask_base_tests_cases import TestFlaskBase


class TestUserBP(TestFlaskBase):
    def test_api_deve_registrar_usuario_na_base(self):
        user = {
            'username': 'test',
            'password': '1234'
        }

        esperado = {
            'id': '1',
            'username': 'test'
        }
        response = self.client.post(url_for('user.register'), json=user)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['username'], esperado['username'])

    def test_api_nao_deve_registrar_usuario_na_base_quando_faltar_fields(self):
        user = {
            'username': 'test',
        }

        esperado = {'password': ['Missing data for required field.']}

        response = self.client.post(url_for('user.register'), json=user)
        self.assertEqual(response.status_code, 401)

        self.assertEqual(response.json, esperado)
