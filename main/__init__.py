from apispec import APISpec
# from apispec_webframeworks.flask import FlaksPlugin
from apispec.ext.marshmallow import MarshmallowPlugin
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_apispec.extension import FlaskApiSpec
import os


pjt_dir = f'{os.getcwd()}/main/default.cfg'

docs = FlaskApiSpec()
db = SQLAlchemy()
api = Api()

def create_app(config_folder=pjt_dir):
    app = Flask(__name__)
    app.config.from_pyfile(pjt_dir)
    app.config.update({
        'APISPEC_SPEC': APISpec(
            title='Board CRUD',
            version='v1',
            openapi_version='2.0',
            plugins=[MarshmallowPlugin()]
        ),
        'APISPEC_SWAGGER_UI_URL': '/docs/'
    })

    docs.init_app(app)
    db.init_app(app)
    api.init_app(app)

    # register blueprints

    with app.app_context():
        from main.controllers import board_bp
        blueprints = [
            board_bp
        ]

        for bp in blueprints:
            app.register_blueprint(bp)

        docs.register_existing_resources()

        for k, v in docs.spec._paths.items():
            docs.spec._paths[k] = {
                inner_key: inner_value for inner_key, inner_value in v.items() if inner_key != 'options'
            }

    return app