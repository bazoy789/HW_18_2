from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service

genres_schema = GenreSchema(many=True)
genre_schema = GenreSchema()
genres_ns = Namespace('genres')

@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genre = genre_service.get_all()
        return genres_schema.dump(all_genre), 200

@genres_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        one_genre = genre_service.get_one(gid)
        return genre_schema.dump(one_genre), 200
