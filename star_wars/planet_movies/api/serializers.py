from rest_framework import serializers
from planet_movies.models import Movie, Planet

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Movie
        fields = '__all__'
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)


class PlanetSerializer(serializers.ModelSerializer):
    # films = serializers.StringRelatedField(many=False, read_only=False, queryset=Movie.objects.all())
    # films= MovieSerializer(read_only=False,many=True)
    # films = serializers.PrimaryKeyRelatedField( many=True, read_only=False, queryset=Movie.objects.all())
    # films = serializers.StringRelatedField( many=True)

    # movies= MovieSerializer(read_only=True,many=True)
    # films = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all(), write_only=True)
    # films = serializers.SlugRelatedField(
    #     many=False,
    #     read_only=False,
    #     slug_field='title', 
    #     required=False,
    #     queryset=Movie.objects.all()
    # )
    class Meta:
        model = Planet
        fields = ['name','films',]
        # fields = '__all__'
    # def get_validation_exclusions(self, *args, **kwargs):
    #     exclusions = super(PlanetSerializer, self).get_validation_exclusions()

    #     return exclusions 

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