from flask import Blueprint, request, jsonify, current_app
from .serealizer import UserSchema


bp_user = Blueprint('user', __name__)


@bp_user.route('/create-user', methods=['POST'])
def register():
    # import ipdb; ipdb.set_trace()

    us = UserSchema()

    user, error = us.load(request.json)

    if error:
        return jsonify(error), 401

    user.gen_hash()

    current_app.db.session.add(user)
    current_app.db.session.commit()

    return us.jsonify(user), 201
