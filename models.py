from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from models import db, Episode, Guest, Appearance  # Assuming models are in a file named models.py


app = Flask(__name__)
api = Api(app)

class Episode(db.Model):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)

    appearances = db.relationship('Apperance', backref='episode', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "number": self.number,
            "appearances": [appearance.to_dict() for appearance in self.appearances]
        }
    
class Guest(db.Model):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String, nullable=False)

    appearances = db.relationship('Appearance', backref='guest', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "occupation": self.occupation
        }
    
class Appearance(db.Model):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "rating": self.rating,
            "episode_id": self.episode_id,
            "guest_id": self.guest_id,
            "episode": self.episode.to_dict(),
            "guest": self.guest.to_dict()
        }
    
    @validates('rating')
    def validate_rating(self, key, rating):
        if rating < 1 or rating > 5:
            raise ValueError("rating must be between 1 and 5")
        return rating
    
# Route for /episodes (List All Episodes)
class EpisodeList(Resource):
    def get(self):
        episodes = Episode.query.all()
        return jsonify([episode.to_dict() for episode in episodes])

# Route for /episodes/:id (Get One Episode with Appearances)
class EpisodeDetail(Resource):
    def get(self, id):
        episode = Episode.query.get(id)
        if episode:
            return jsonify(episode.to_dict())
        return jsonify({"error": "Episode not found"}), 404

# Route for /guests (List All Guests)
class GuestList(Resource):
    def get(self):
        guests = Guest.query.all()
        return jsonify([guest.to_dict() for guest in guests])

# Route for /appearances (Create a New Appearance)
class AppearanceCreate(Resource):
    def post(self):
        data = request.get_json()
        rating = data.get('rating')
        episode_id = data.get('episode_id')
        guest_id = data.get('guest_id')

        # Create new appearance
        appearance = Appearance(rating=rating, episode_id=episode_id, guest_id=guest_id)

        try:
            db.session.add(appearance)
            db.session.commit()
            return jsonify(appearance.to_dict()), 201
        except ValueError as e:
            return jsonify({"errors": [str(e)]}), 400
        except Exception as e:
            return jsonify({"errors": [str(e)]}), 500

# Add the resources to the API
api.add_resource(EpisodeList, '/episodes')
api.add_resource(EpisodeDetail, '/episodes/<int:id>')
api.add_resource(GuestList, '/guests')
api.add_resource(AppearanceCreate, '/appearances')

if __name__ == '__main__':
    app.run(debug=True)