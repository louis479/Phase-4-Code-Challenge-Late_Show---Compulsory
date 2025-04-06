from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_migrate import Migrate
from models import db

api = Api()
migrate = Migrate()  # Instantiate Migrate here

class HomePage(Resource):
    def get(self):
        return {"message": "Welcome to the API! Use /episodes, /guests, or /appearances for data."}


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    api.init_app(app)
    migrate.init_app(app, db)  # Correct way to use Migrate in factory

    # Import models in models.py to ensure they're registered with SQLAlchemy
    from models.models import Episode, Guest, Appearance

    # Register routes
    from routes import register_routes
    register_routes(api)

    # Experienced error when using class resource so unfortunately used function routes
    @app.route("/")
    def home():
        return "Welcome to the API!"

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
