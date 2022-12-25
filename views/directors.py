from flask_restx import Resource, Namespace

from dao.model.directors import DirectorSchema
from implemented import director_service

directors_schema = DirectorSchema(many=True)
director_schema = DirectorSchema()
directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200

@directors_ns.route('/<int:gid>')
class DirectorView(Resource):
    def get(self, gid):
        one_directors = director_service.get_one(gid)
        return director_schema.dump(one_directors), 200
