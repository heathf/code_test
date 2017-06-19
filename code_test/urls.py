"""
	Route information for our code_test app
"""

from .api import MovieViewSet, GenreViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'genres', GenreViewSet)

urlpatterns = router.urls
