from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_director_id(self, data):
        return self.session.query(Movie).filter(Movie.director_id == data).all()

    def get_by_genre_id(self, data):
        return self.session.query(Movie).filter(Movie.genre_id == data).all()

    def get_by_year(self, data):
        return self.session.query(Movie).filter(Movie.year == data).all()

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update(self, data):
        mid = data.get('id')
        movie = self.session.query(Movie).filter(Movie.id == mid).update(data)
        self.session.commit()
        return movie

    def delete(self, mid):
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()
