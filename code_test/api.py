"""
	Our view for the code_test api.
"""

import functools

from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from .serializers import MovieSerializer, GenreSerializer
from .models import Movie, Genre


class MovieViewSet(ModelViewSet):
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = ('genre_id', 'name')

	@detail_route(methods=['get'], url_path='get-number-of-sequels')
	def	get_number_of_sequels(self, request, pk=None):
		"""
		Will retrieve a list of movies that are sequels for the provided movie.  It determines this by looking for
		movies that contain the name of the provided movie

		:param request: The received request object
		:type request: rest_framework.request.Request
		:param pk: The primary key for the movie to look for sequels for
		:type pk: int
		:return: A dict with a number_of_sequels key and also a sequels key
		:rtype: rest_framework.response.Response
		"""
		movie = Movie.objects.filter(pk=pk).first()
		sequels = self.get_sequels(movie)
		converted_sequels = [{'name': s.name, 'year': s.year} for s in sequels]

		sequel_data = {
			'number_of_sequels': len(sequels),
			'sequels': converted_sequels
		}
		return Response(data=sequel_data)

	def get_sequels(self, movie):
		"""
		This is a helper function for get_number_of_sequels.  It obtains the movies that contain the string ``movie``

		:param movie: The movie for which to obtain the sequel information for
		:type movie: models.Movie
		:return: A list of movies that contain the string ``movie``
		:rtype:  list
		"""
		movies = Movie.objects.filter(name__contains=movie.name)
		print len(movies)
		return [m for m in movies if m.name.lower().strip() != movie.name.lower()]


class GenreViewSet(ModelViewSet):
	queryset = Genre.objects.all()
	serializer_class = GenreSerializer

	@detail_route(methods=['get'], url_path='get-most-genres-year')
	def get_most_genres_year(self, request, pk=None):
		"""
		Will find which genre had the most movies for a given year

		:param request: The received request object
		:type request: rest_framework.request.Request
		:param pk: The primary key for the genre
		:type pk: int
		:return: A dictionary with genre, count and year keys with their corresponding values
		:rtype: rest_framework.response.Response
		"""
		year = self.request.query_params.get('year', None)
		movies = Movie.objects.filter(year=year)
		sums = []
		genres = {m.genre for m in movies}

		for genre in genres:
			mapped = map(functools.partial(self.get_movie_by_genre, genre=genre), movies)
			sums.append({
				'genre': genre.name,
				'count': len([m for m in mapped if m])
			})

		item = max(sums)

		return Response(data={
			'genre': item['genre'],
			'count': item['count'],
			'year': year
		})

	def get_movie_by_genre(self, movie, genre):
		"""
		This is a helper function to be used in conjunction with map and functools.partial to count movies for a
		given genre

		:param movie: The movie to test the genre for
		:type movie: models.Movie
		:param genre: The name of the genre for which to see if ``movie`` is a member of
		:type genre: str
		:return: True if the movie is of genre ``genre``, otherwise False
		:rtype: bool
		"""
		return movie.genre == genre


