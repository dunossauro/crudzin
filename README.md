# Crudzin

Experiência com um crud usando flask e suas ferramentas

- Flask
- flask_sqlalchemy
- flask_migrate
- flask_marshmallow
- marshmallow_sqlalchemy

## Apoie a Live de Python

apoia.se/livedepython


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
