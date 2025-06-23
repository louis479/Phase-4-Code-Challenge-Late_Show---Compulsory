from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_migrate import Migrate
from models import db

import os
basedir = os.path.abspath(os.path.dirname(__file__))

api = Api()
migrate = Migrate()  # Instantiate Migrate here

class HomePage(Resource):
    def get(self):
        return {"message": "Welcome to the API! Use /episodes, /guests, or /appearances for data."}


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance', 'app.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    api.init_app(app)
    migrate.init_app(app, db)  

    # Register routes
    with app.app_context():
        from routes import register_routes
        register_routes(api)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
