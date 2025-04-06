from flask import jsonify, request
from flask_restful import Resource
from models.models import db, Episode, Guest, Appearance

class EpisodeList(Resource):
    def get(self):
        episodes = Episode.query.all()
        return jsonify([ep.to_dict() for ep in episodes])

class EpisodeDetail(Resource):
    def get(self, id):
        episode = Episode.query.get(id)
        if episode:
            return jsonify(episode.to_dict())
        return jsonify({"error": "Episode not found"}), 404

class GuestList(Resource):
    def get(self):
        guests = Guest.query.all()
        return jsonify([guest.to_dict() for guest in guests])

class AppearanceCreate(Resource):
    def post(self):
        data = request.get_json()
        try:
            rating = data["rating"]
            episode_id = data["episode_id"]
            guest_id = data["guest_id"]

            appearance = Appearance(rating=rating, episode_id=episode_id, guest_id=guest_id)
            db.session.add(appearance)
            db.session.commit()
            return jsonify(appearance.to_dict()), 201
        except ValueError as e:
            return jsonify({"errors": [str(e)]}), 400
        except Exception as e:
            return jsonify({"errors": [str(e)]}), 500

def register_routes(api):
    api.add_resource(EpisodeList, "/episodes")
    api.add_resource(EpisodeDetail, "/episodes/<int:id>")
    api.add_resource(GuestList, "/guests")
    api.add_resource(AppearanceCreate, "/appearances")
