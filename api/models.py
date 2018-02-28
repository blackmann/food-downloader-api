from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.TextField()
    directions = models.TextField()
    image = models.CharField(max_length=300)
    video = models.CharField(max_length=300, blank=True)
    level = models.CharField(max_length=50, default="Easy")
    author = models.CharField(max_length=70, default="Telande")
    popularity = models.IntegerField(default=0)
    estimated_time = models.IntegerField() # time in seconds
    utensils = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['popularity', ]
