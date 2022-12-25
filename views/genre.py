from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import director_service

genre_schema = GenreSchema(many=True)

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get_all(self):
        all_directors = director_service.get_all()
        return director_schema.dump(all_directors), 200

@director_ns.route('/<int:gid>')
class DirectorView(Resource):
    def get_one(self, gid):
        one_directors = director_service.get_one(gid)
        return director_schema.dump(one_directors), 200