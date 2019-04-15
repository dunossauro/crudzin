# Crudzin

Experiência com um crud usando flask e suas ferramentas

- Flask
- flask_sqlalchemy
- flask_migrate
- flask_marshmallow
- marshmallow_sqlalchemy
- flask-jwt-extended

## Apoie a Live de Python

apoia.se/livedepython

## Vídeos onde o projeto foi desenvolvido

[Desenvolvimento inicial](https://www.youtube.com/watch?v=WzaKIRJBGXo)

[Escrevendo os testes](https://www.youtube.com/watch?v=jqDxDsRJtAo)

[Autenticando a API](https://youtu.be/ieGA91ExOH0)

[Testes de comportamento com BDD](https://youtu.be/aX0P5tsiat4)

## Como rodar esse projeto

```sh
export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True

flask run
```

## Como fazer as migrações

```sh
flask db init
flask db migrate
flask db upgrade
```


## Como rodar os testes e obter cobertura

```sh
# gera o report e roda os testes
coverage run --source=app -m unittest discover -s tests/ -v
# mostra um resumo da cobertura em shell
coverage report
# gera o path '/htmlcov' com htmls estáticos da cobertura
coverage html
```

## Como rodar os testes de comportamento com BDD

```sh
behave tests/behavior_tests/features/
```
