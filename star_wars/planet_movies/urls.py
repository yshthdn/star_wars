from planet_movies.views import MovieViewSet
from  rest_framework.routers import DefaultRouter
from .views import MovieViewSet, PlanetViewSet

router = DefaultRouter()
router.register(
    r'movies',
    MovieViewSet,
    basename = 'movies'
)

router.register(
    r'planet',
    PlanetViewSet,
    basename = 'planet'
)