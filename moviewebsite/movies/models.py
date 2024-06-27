from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    poster = models.ImageField(upload_to='poster/')
    description = models.TextField()
    release_date = models.DateField()
    actors = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    trailer_link = models.URLField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.movie.title} - {self.user.username}'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(Movie, related_name='favorited_by')

    def __str__(self):
        return self.user.username
