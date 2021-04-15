from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Planet(models.Model):
    name = models.CharField(max_length=500)
    films = models.ManyToManyField(Movie, related_name='planet_in_movie')

    def __str__(self):
        return self.name
