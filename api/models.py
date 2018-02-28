from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.TextField()
    directions = models.TextField()
    image = models.CharField(max_length=300)
    video = models.CharField(max_length=300)
    level = models.CharField(max_length=50)
    author = models.CharField(max_length=70)
    popularity = models.IntegerField()
    estimated_time = models.IntegerField() # time in seconds

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['popularity', ]
