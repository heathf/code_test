from django.test import TestCase
from code_test.models import Movie, Genre
import unittest
import requests
import socket

class TestApi(unittest.TestCase):
	def setUp(self):
		"""
		Will make sure the Django dev server is running

		:return: None
		:rtype: None
		"""
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		try:
			s.bind(("127.0.0.1", 8000))
			s.close()
			should_fail = True
		except socket.error as e:
			should_fail = False

		if should_fail:
			self.fail("Please start the Django development server on port 8000 and re-invoke the tests")

	def create_movie(self, name="Test Movie", year=2000, genre_id=50):
		"""
		Will create a new movie

		:param name: Name of the movie
		:type name: str
		:param year: The movie's year
		:type year: int
		:param genre_id: The ID of the genre for the movie
		:type genre_id: int
		:return: The newly created movie
		:rtype: code_test.models.Movie
		"""
		genre = Genre.objects.filter(pk=genre_id).first()
		return Movie.objects.create(name=name, year=year, genre=genre)

	def create_genre(self, name="Test Genre"):
		"""
		Will create a new genre in the DB

		:param name: Name of the genre
		:type name: str
		:return: The newly created genre
		:rtype: code_test.models.Genre
		"""
		return Genre.objects.create(name=name)

	def test_movie_creation(self):
		"""
		Will test the creation of a new movie

		:return: None
		:rtype: None
		"""
		movie = self.create_movie()
		self.assertTrue(isinstance(movie, Movie))

	def test_genre_creation(self):
		"""
		Will test the creation of a new genre

		:return: None
		:rtype: None
		"""
		genre = self.create_genre()
		self.assertTrue(isinstance(genre, Genre))

	def test_movie_update(self, name="New Movie Name"):
		"""
		Will test updating a movie record

		:param name: The new name of the movie
		:type name: str
		:return: None
		:rtype: None
		"""
		updated_id = Movie.objects.update(name=name)
		updated_movie = Movie.objects.filter(pk=updated_id).first()
		self.assertTrue(updated_movie.name, name)

	def test_genre_update(self, name="New Genre Name"):
		"""
		Will test updating a genre with a new name

		:param name: The new name for the genre
		:type name: str
		:return: None
		:rtype: None
		"""
		updated_id = Genre.objects.update(name=name)
		updated_genre = Genre.objects.filter(pk=updated_id).first()
		self.assertTrue(updated_genre.name, name)

	def test_number_of_sequels(self):
		"""
		Will test obtaining the number of sequels for a given movie

		:return: None
		:rtype: None
		"""
		pk = 1299
		response = requests.get('http://127.0.0.1:8000/code_test/movies/{}/get-number-of-sequels/'.format(pk))
		self.assertEqual(response.status_code, 200)

	def test_most_genres_year(self):
		"""
		Will test obtaining which genre had the most movies for a given year

		:return: None
		:rtype: None
		"""
		pk = 50
		url = 'http://127.0.0.1:8000/code_test/genres/{}/get-most-genres-year/?year=2000'.format(pk)
		response = requests.get(url)
		self.assertEqual(response.status_code, 200)


