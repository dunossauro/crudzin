from json import loads
from behave import given, when, then
from flask import url_for
from app.model import User


@given(u'que o usuário {username} não exista na base de dados')
def check_user_in_database(context, username):
    assert not User.query.filter_by(
        username=username
    ).first()


@when('efetuar o cadastro do usuário')
def register_user(context):
    context.last_request = context.client.post(
        url_for('user.register'), json=loads(context.text)
    )


@then('a seguinte mensagem deve ser exibida')
def assert_api_message(context):
    """Melhorar isso aqui."""
    assert context.last_request.json == loads(context.text)
