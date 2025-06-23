from flask import Flask, send_from_directory
# from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_migrate import Migrate
from models import db
import os

basedir = os.path.abspath(os.path.dirname(__file__))


# class HomePage(Resource):
#     def get(self):
#         return {
#             "message": "Welcome to the Late Show API",
#             "endpoints": {
#                 "episodes": "/episodes",
#                 "guests": "/guests",
#                 "appearances": "/appearances"
#             }
#         }

def create_app():
    app = Flask(__name__)

    os.makedirs(os.path.join(basedir, 'instance'), exist_ok=True)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'instance', 'app.db')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    api = Api(app)
    migrate = Migrate(app, db)  
    
    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')
    
    # Register routes
    with app.app_context():
        from routes import register_routes
        register_routes(api)

        from models.model import Episode, Guest, Appearance
        db.create_all()  # Ensure the database is created
        # try:
        #     db.create_all()  # Ensure the database is created
        # except Exception as e:
        #     print(f"Error creating database: {e}")  

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)


