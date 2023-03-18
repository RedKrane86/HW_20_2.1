import pytest
from unittest.mock import MagicMock

from implemented import director_dao
from implemented import genre_dao
from implemented import movie_dao
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie


@pytest.fixture
def director_dao():
    john = Director(id=1, name='john')
    kate = Director(id=2, name='kate')
    jack = Director(id=3, name='jack')

    director_dao.get_all = MagicMock(return_value=[john, kate, jack])
    director_dao.get_one = MagicMock(return_value=Director(id=1))
    director_dao.create = MagicMock(return_value=Director(id=2))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao


@pytest.fixture
def genre_dao():
    g1 = Genre(id=1, name='ha-ha')
    g2 = Genre(id=2, name='hi-hi')
    g3 = Genre(id=3, name='ho-ho')

    genre_dao.get_all = MagicMock(return_value=[g1, g2, g3])
    genre_dao.get_one = MagicMock(return_value=Genre(id=1))
    genre_dao.create = MagicMock(return_value=Genre(id=2))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao


@pytest.fixture
def movie_dao():
    m1 = Movie(
        id=1,
        title='movie1',
        description='movie1 description',
        trailer='movie1 trailer',
        year=2021,
        rating=11,
        genre_id=1,
        director_id=1
        )
    m2 = Movie(
        id=2,
        title='movie2',
        description='movie2 description',
        trailer='movie2 trailer',
        year=2022,
        rating=12,
        genre_id=2,
        director_id=2
    )
    m3 = Movie(
        id=3,
        title='movie3',
        description='movie3 description',
        trailer='movie3 trailer',
        year=2023,
        rating=13,
        genre_id=3,
        director_id=3
    )

    movie_dao.get_all = MagicMock(return_value=[m1, m2, m3])
    movie_dao.get_one = MagicMock(return_value=Movie(id=1))
    movie_dao.create = MagicMock(return_value=Movie(id=2))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao
