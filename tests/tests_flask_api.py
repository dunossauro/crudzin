from base_test_classes import TestFlaskLoged
from flask import url_for


class TestCadastro(TestFlaskLoged):
    def test_cadastrar_deve_retornar_o_payload_enviado_sem_id(self):
        dado = {
            'livro': 'Python 3',
            'escritor': 'Eduardo'
        }

        response = self.client.post(
            url_for('books.cadastrar'), json=dado, headers=self.header
        )

        response.json.pop('id')

        self.assertEqual(dado, response.json)

    def test_cadastrar_deve_retornar_erro_quando_o_payload_for_incompleto(self):
        dado = {
            'livro': 'Python 3',
        }

        esperado = {'escritor': ['Missing data for required field.']}
        response = self.client.post(
            url_for('books.cadastrar'), json=dado, headers=self.header
        )

        self.assertEqual(esperado, response.json)

    def test_cadastrar_deve_retornar_erro_quando_o_payload_contiver_a_chave_id(self):
        dado = {
            'livro': 'Python 3',
            'escritor': 'Eduardo',
            'id': 1
        }

        esperado = {'id': ['Não envie pelo amor de deus o ID']}
        response = self.client.post(
            url_for('books.cadastrar'), json=dado, headers=self.header
        )

        self.assertEqual(esperado, response.json)


class TestMostrar(TestFlaskLoged):
    def test_mostrar_deve_retornar_uma_query_vazia(self):
        response = self.client.get(
            url_for('books.mostrar'), headers=self.header
        )
        self.assertEqual([], response.json)

    def test_mostrar_deve_retornar_um_query_com_elemento_iserido(self):
        dado = {
            'livro': 'Python 3',
            'escritor': 'Eduardo'
        }

        response = self.client.post(
            url_for('books.cadastrar'), json=dado, headers=self.header
        )
        response = self.client.post(
            url_for('books.cadastrar'), json=dado, headers=self.header
        )

        response = self.client.get(
            url_for('books.mostrar'), headers=self.header
        )
        self.assertEqual(2, len(response.json))


class TestDeletar(TestFlaskLoged):
    def test_deletar_deve_retornar_deletado_quando_nao_encontrar_regristro(self):
        response = self.client.get(
            url_for('books.deletar', identificador=1), headers=self.header
        )

        self.assertEqual(response.json, 'Deletado!!!!')


    def test_deletar_deve_retornar_deletado_quando_encontrar_registro_na_base(self):
        dado = {
            'livro': 'Python 3',
            'escritor': 'Eduardo'
        }

        self.client.post(url_for('books.cadastrar'), json=dado)

        response = self.client.get(
            url_for('books.deletar', identificador=1), headers=self.header
        )

        self.assertEqual(response.json, 'Deletado!!!!')


class Testmodificar(TestFlaskLoged):
    def test_modificar_(self):
        identificador = 1
        estado_inicial = {
            'livro': 'Python 3',
            'escritor': 'Eduardo'
        }

        estado_final = {
            'livro': 'Python 2 não é melhor que 3',
        }
        self.client.post(
            url_for('books.cadastrar'),
            json=estado_inicial,
            headers=self.header
        )

        response = self.client.post(
            url_for('books.modificar', identificador=1),
            json=estado_final,
            headers=self.header
        )
        self.assertEqual(estado_final['livro'], response.json['livro'])
        self.assertEqual(identificador, response.json['id'])
