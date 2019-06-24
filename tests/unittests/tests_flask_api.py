from flask import url_for
from flask_base_tests_cases import TestFlaskBase


class TestCadastro(TestFlaskBase):
    def test_cadastrar_deve_retornar_o_payload_enviado_sem_id(self):
        dado = {
            'livro': 'Python 3',
            'escritor': {'name': 'Eduardo'}
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
            'escritor': {'name': 'Eduardo'},
            'id': 1
        }

        esperado = {'id': ['Não envie pelo amor de deus o ID']}
        response = self.client.post(url_for('books.cadastrar'), json=dado)

        self.assertEqual(esperado, response.json)


class TestMostrar(TestFlaskBase):
    def test_mostrar_deve_retornar_uma_query_vazia(self):
        self.create_user()
        token = self.create_token()
        # from time import sleep
        # sleep(2) -> sleep de testes para ver o token ficar inválido
        response = self.client.get(
            url_for('books.mostrar'),
            headers=token
        )
        self.assertEqual([], response.json)

    def test_mostrar_deve_retornar_um_query_com_elemento_iserido(self):
        dado = {
            'livro': 'Python 3',
            'escritor': {'name': 'Eduardo'}
        }
        self.create_user()
        token = self.create_token()
        response = self.client.post(url_for('books.cadastrar'), json=dado)
        response = self.client.post(url_for('books.cadastrar'), json=dado)

        response = self.client.get(url_for('books.mostrar'), headers=token)
        self.assertEqual(2, len(response.json))


class TestDeletar(TestFlaskBase):
    def test_deletar_deve_retornar_deletado_quando_nao_encontrar_regristro(self):
        response = self.client.get(url_for('books.deletar', identificador=1))

        self.assertEqual(response.json, 'Deletado!!!!')


    def test_deletar_deve_retornar_deletado_quando_encontrar_registro_na_base(self):
        dado = {
            'livro': 'Python 3',
            'escritor': {'name': 'Eduardo'}
        }

        self.client.post(url_for('books.cadastrar'), json=dado)

        response = self.client.get(url_for('books.deletar', identificador=1))

        self.assertEqual(response.json, 'Deletado!!!!')


class Testmodificar(TestFlaskBase):
    def test_modificar_(self):
        identificador = 1
        estado_inicial = {
            'livro': 'Python 3',
            'escritor': {'name': 'Eduardo'}
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
