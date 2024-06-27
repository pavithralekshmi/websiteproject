# movies/admin.p
from django.contrib import admin
from .models import Movie, Review, UserProfile, Category

admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(UserProfile)
admin.site.register(Category)