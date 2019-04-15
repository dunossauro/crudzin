# language:pt
Funcionalidade: Cadastro
  Eu como um usuário
  Desejo me cadastrar no sistema

Contexto: Criar o usuário
  Dado que o usuário sejá criado

Cenário: Payload sem password
  Dado que o usuário Test não exista na base de dados
  Quando efetuar o cadastro do usuário
    """
    {
      "username": "Test"
    }
    """
  Então a seguinte mensagem deve ser exibida
    """
    {"password": ["Missing data for required field."]}
    """

Cenário: Payload sem username
  Dado que o usuário Test não exista na base de dados
  Quando efetuar o cadastro do usuário
    """
    {
      "password": "123"
    }
    """
  Então a seguinte mensagem deve ser exibida
    """
    {"username": ["Missing data for required field."]}
    """

Cenário: Payload vazio
  Dado que o usuário Test não exista na base de dados
  Quando efetuar o cadastro do usuário
    """
    {}
    """
  Então a seguinte mensagem deve ser exibida
    """
    {
      "username": ["Missing data for required field."],
      "password": ["Missing data for required field."]
    }
    """

Cenário: Payload com password inteiro
  Dado que o usuário Test não exista na base de dados
  Quando efetuar o cadastro do usuário
    """
    {"username": "Test", "password": 123}
    """
  Então a seguinte mensagem deve ser exibida
    """
      {"password": ["Not a valid string."]}
    """

Cenário: Cadastro com sucesso
  Dado que o usuário Test não exista na base de dados
  Quando efetuar o cadastro do usuário
    """
    {"username": "Test", "password": "123"}
    """
  Então a seguinte mensagem deve ser exibida
    """
    {
      "id": 1,
      "username": "Test",
      "password": "<>"
    }
    """
