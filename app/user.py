from flask import Blueprint, g, jsonify, request, current_app
from .login import auth
from .serealizer import UserSchema

bp_user = Blueprint('user', __name__)


@bp_user.route('/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(600)
    return jsonify({'token': token.decode('ascii'), 'duration': 600})


@bp_user.route('/create-user', methods=['POST'])
def create_user():
    us = UserSchema()

    user, error = us.load(request.json)

    if error:
        return jsonify(error), 401

    user.hash_password(request.json['password'])

    current_app.db.session.add(user)
    current_app.db.session.commit()

    return us.jsonify(user), 201
