from rest_framework import serializers
from planet_movies.models import Movie, Planet

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Movie
        fields = '__all__'
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)


class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = ['name','films',]
  

    def to_representation(self, value):
        titles = []
        for movie in value.films.all():
            titles.append(movie.title)
        films_titles = ()
        return str(value.name) + " in films " + str(titles)
    def create(self, validated_data):
        films = validated_data.pop('films')

        planet = Planet.objects.create(**validated_data)
        for film in films:
            planet.films.add(film)
        return planet