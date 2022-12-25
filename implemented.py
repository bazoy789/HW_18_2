from dao.directors import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO

from service.directors import DirectorService
from service.genre import GenreService
from service.movie import MovieService

from setup_db import db

movie_dao = MovieDAO(db.session)
director_dao = DirectorDAO(db.session)
genre_dao = GenreDAO(db.session)

movie_service = MovieService(movie_dao)
director_service = DirectorService(director_dao)
genre_service = GenreService(genre_dao)
