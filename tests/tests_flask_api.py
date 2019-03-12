from unittest import TestCase
from flask import url_for
from app import create_app


class TestFlaskBase(TestCase):
    def setUp(self):
        """Roda antes de todos os testes."""
        self.app = create_app()
        self.app.testing = True
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.app.db.create_all()


    def tearDown(self):
        """Roda depois de todos os testes."""
        self.app.db.drop_all()


class TestCadastro(TestFlaskBase):
    def test_cadastrar_deve_retornar_o_payload_enviado_sem_id(self):
        dado = {
            'livro': 'Python 3',
            'escritor': 'Eduardo'
        }

        response = self.client.post(url_for('books.cadastrar'), json=dado)

        response.json.pop('id')

        self.assertEqual(dado, response.json)

    def test_cadastrar_deve_retornar_erro_quando_o_payload_for_incompleto(self):
        dado = {
            'livro': 'Python 3',
        }

        esperado = {'escritor': ['Missing data for required field.']}
        response = self.client.post(url_for('books.cadastrar'), json=dado)

        self.assertEqual(esperado, response.json)

    def test_cadastrar_deve_retornar_erro_quando_o_payload_contiver_a_chave_id(self):
        dado = {
            'livro': 'Python 3',
            'escritor': 'Eduardo',
            'id': 1
        }

        esperado = {'id': ['Não envie pelo amor de deus o ID']}
        response = self.client.post(url_for('books.cadastrar'), json=dado)

        self.assertEqual(esperado, response.json)

class TestMostrar(TestFlaskBase):
    def test_mostrar_deve_retornar_uma_query_vazia(self):
        response = self.client.get(url_for('books.mostrar'))
        self.assertEqual([], response.json)

    def test_mostrar_deve_retornar_um_query_com_elemento_iserido(self):
        dado = {
            'livro': 'Python 3',
            'escritor': 'Eduardo'
        }

        response = self.client.post(url_for('books.cadastrar'), json=dado)
        response = self.client.post(url_for('books.cadastrar'), json=dado)

        response = self.client.get(url_for('books.mostrar'))
        self.assertEqual(2, len(response.json))


class TestDeletar(TestFlaskBase):
    def test_deletar_deve_retornar_deletado_quando_nao_encontrar_regristro(self):
        response = self.client.get(url_for('books.deletar', identificador=1))

        self.assertEqual(response.json, 'Deletado!!!!')


    def test_deletar_deve_retornar_deletado_quando_encontrar_registro_na_base(self):
        dado = {
            'livro': 'Python 3',
            'escritor': 'Eduardo'
        }

        self.client.post(url_for('books.cadastrar'), json=dado)

        response = self.client.get(url_for('books.deletar', identificador=1))

        self.assertEqual(response.json, 'Deletado!!!!')


class Testmodificar(TestFlaskBase):
    def test_modificar_(self):
        identificador = 1
        estado_inicial = {
            'livro': 'Python 3',
            'escritor': 'Eduardo'
        }

        estado_final = {
            'livro': 'Python 2 não é melhor que 3',
        }
        self.client.post(url_for('books.cadastrar'), json=estado_inicial)

        response = self.client.post(
            url_for('books.modificar', identificador=1), json=estado_final
        )
        # import ipdb; ipdb.set_trace()
        self.assertEqual(estado_final['livro'], response.json['livro'])
        self.assertEqual(identificador, response.json['id'])
