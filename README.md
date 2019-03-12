# Crudzin

Experiência com um crud usando flask e suas ferramentas

- Flask
- flask_sqlalchemy
- flask_migrate
- flask_marshmallow
- marshmallow_sqlalchemy

## Apoie a Live de Python

apoia.se/livedepython

## Vídeos onde o projeto foi desenvolvido

[Desenvolvimento inicial](https://www.youtube.com/watch?v=WzaKIRJBGXo)

[Escrevendo os testes](https://www.youtube.com/watch?v=jqDxDsRJtAo)
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
