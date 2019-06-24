from marshmallow import fields, validates, ValidationError
from flask_marshmallow import Marshmallow
from .model import Book, User, Escritor

ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class EscritorSchema(ma.ModelSchema):
    class Meta:
        model = Escritor

    name = fields.Str(required=True)


class BookSchema(ma.ModelSchema):
    class Meta:
        model = Book

    livro = fields.Str(required=True)
    escritor = ma.Nested(EscritorSchema)

    @validates('id')
    def validate_id(self, value):
        raise ValidationError('Não envie pelo amor de deus o ID')


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User

    username = fields.Str(required=True)
    password = fields.Str(required=True)
