from marshmallow import fields, validates, ValidationError
from flask_marshmallow import Marshmallow
from .model import Book

ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class BookSchema(ma.ModelSchema):
    class Meta:
        model = Book

    livro = fields.Str(required=True)
    escritor = fields.Str(required=True)

    @validates('id')
    def validate_id(self, value):
        raise ValidationError('Não envie pelo amor de deus o ID')
