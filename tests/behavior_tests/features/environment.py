import ipdb
from app import create_app


def before_feature(context, feature):
    context.flask = create_app()
    context.flask.testing = True
    context.flask_context = context.flask.test_request_context()
    context.flask_context.push()
    context.client = context.flask.test_client()
    context.flask.db.create_all()


def after_feature(context, feature):
    context.flask.db.drop_all()


def after_step(context, step):
    if step.status == 'failed':
        ipdb.spost_mortem(step.exc_traceback)
