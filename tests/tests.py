from django.test import TestCase
from code_test.models import Movie, Genre
import unittest
import requests

class TestApi(unittest.TestCase):
	def create_movie(self, name="Test Movie", year=2000, genre_id=50):
		genre = Genre.objects.filter(pk=genre_id).first()
		return Movie.objects.create(name=name, year=year, genre=genre)

	def create_genre(self, name="Test Genre"):
		return Genre.objects.create(name=name)

	def test_movie_creation(self):
		movie = self.create_movie()
		self.assertTrue(isinstance(movie, Movie))

	def test_genre_creation(self):
		genre = self.create_genre()
		self.assertTrue(isinstance(genre, Genre))

	def test_movie_update(self, name="New Movie Name"):
		updated_id = Movie.objects.update(name=name)
		updated_movie = Movie.objects.filter(pk=updated_id).first()
		self.assertTrue(updated_movie.name, name)

	def test_genre_update(self, name="New Genre Name"):
		updated_id = Genre.objects.update(name=name)
		updated_genre = Genre.objects.filter(pk=updated_id).first()
		self.assertTrue(updated_genre.name, name)

	def test_number_of_sequels(self):
		pk = 1299
		response = requests.get('http://127.0.0.1:8000/code_test/movies/{}/get-number-of-sequels/'.format(pk))
		self.assertEqual(response.status_code, 200)

	def test_most_genres_year(self):
		pk = 50
		url = 'http://127.0.0.1:8000/code_test/genres/{}/get-most-genres-year/?year=2000'.format(pk)
		response = requests.get(url)
		self.assertEqual(response.status_code, 200)

