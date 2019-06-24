from flask import Blueprint, current_app, request, jsonify
from flask_jwt_extended import jwt_required
from .model import Book
from .serealizer import BookSchema


bp_books = Blueprint('books', __name__)


@bp_books.route('/mostrar', methods=['GET'])
@jwt_required
def mostrar():
    result = Book.query.all()
    return BookSchema(many=True).jsonify(result), 200


@bp_books.route('/deletar/<identificador>', methods=['GET'])
def deletar(identificador):
    Book.query.filter(Book.id == identificador).delete()
    current_app.db.session.commit()
    return jsonify('Deletado!!!!')


@bp_books.route('/modificar/<identificador>', methods=['POST'])
def modificar(identificador):
    bs = BookSchema()
    query = Book.query.filter(Book.id == identificador)
    query.update(request.json)
    current_app.db.session.commit()
    return bs.jsonify(query.first())


@bp_books.route('/cadastrar', methods=['POST'])
def cadastrar():
    bs = BookSchema()
    book, error = bs.load(request.json, session=current_app.db.session)

    if error:
        return jsonify(error), 401

    current_app.db.session.add(book)
    current_app.db.session.commit()
    return bs.jsonify(book), 201
