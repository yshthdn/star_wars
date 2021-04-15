from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets, status
from rest_framework.response import Response
from planet_movies.api.serializers import MovieSerializer, PlanetSerializer

from .models import Movie, Planet

class MovieViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Movie.objects.all()
        movie = get_object_or_404(Movie, title=pk)
        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlanetViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Planet.objects.all()
        # import ipdb;ipdb.set_trace()
        serializer = PlanetSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Movie.objects.all()
        movie = get_object_or_404(Movie, title=pk)
        planet = movie.planet_in_movie
        serializer = PlanetSerializer(planet, many=True)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        serializer = PlanetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            # import ipdb;ipdb.set_trace()
            return Response(data={"Success":True}, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    