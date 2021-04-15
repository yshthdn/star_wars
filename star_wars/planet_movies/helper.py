import requests
import json
from planet_movies.api import serializers
from planet_movies.models import Movie, Planet


def add_movies():

    movies_data = requests.get('http://swapi.dev/api/films/')
    movies_data_load = json.loads(movies_data.content)
    serializer = serializers.MovieSerializer(data=movies_data_load['results'], many=True)
    if serializer.is_valid():
        serializer.save()

def add_planets():
    planets_data = requests.get('http://swapi.dev/api/planets/')
    planets_data_load = json.loads(planets_data.content)
    planets_data_new = []
    mfi = Movie.objects.first().id
    for planet in planets_data_load['results']:
        film_list = []
        for film in planet['films']:
            film_list.append(int(film.split('films/')[1].strip('/'))+mfi -1)
        planet['films'] = film_list
        planets_data_new.append(planet)
    serializer = serializers.PlanetSerializer(data=planets_data_new, many=True)
    if serializer.is_valid():
        
        serializer.save()

    
def clean_old_data():
    Movie.objects.all().delete()
    Planet.objects.all().delete()

def update_data():
    try:
        clean_old_data()
        add_movies()
        add_planets()
    except Exception:
        print("Issue updating data!")
