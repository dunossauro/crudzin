from datetime import timedelta
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token
from .model import User
from .serealizer import UserSchema

bp_login = Blueprint('login', __name__)


@bp_login.route('/login', methods=['POST'])
def login():
    user, error = UserSchema().load(request.json)

    if error:
        return jsonify(error), 401

    user = User.query.filter_by(username=user.username).first()

    if user and user.verify_password(request.json['password']):
        acess_token = create_access_token(
            identity=user.id,
            expires_delta=timedelta(seconds=1)
        )
        refresh_token = create_refresh_token(identity=user.id)

        return jsonify({
            'acess_token': acess_token,
            'refresh_token': refresh_token,
            'message': 'sucess'
        }), 200

    return jsonify({
        'message': 'Deu ruim, credenciais invalidas'
    }), 401
