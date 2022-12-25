from flask import request
from flask_restx import Resource, Namespace
from dao.model.movie import MovieSchema
from implemented import movie_service

movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()
movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):

    def get(self):
        director = request.args.get('director_id')
        genre = request.args.get('genre_id')
        year = request.args.get('year')
        filters = {
            'director_id': director,
            'genre_id': genre,
            'year': year,
        }
        all_movies = movie_service.get_all(filters)
        return movies_schema.dump(all_movies), 200

    def post(self):
        reg = request.json
        movie = movie_service.create(reg)
        return '', 201, {"location": f"/movies/{movie.id}"}

@movies_ns.route('/<int:mid>')
class MovieView(Resource):

    def get(self, mid):
        one_movies = movie_service.get_one(mid)
        return movie_schema.dump(one_movies), 200

    def put(self, mid):
        reg = request.json
        if 'id' is not reg:
            reg['id'] = mid
        movie_service.update(reg)
        return '', 204

    def delete(self, mid):
        movie_service.delete(mid)
        return '', 204
