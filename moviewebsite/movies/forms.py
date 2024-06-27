# movies/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Movie, Review, Category


from django import forms
from .models import Movie, Category

class MovieForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True)

    class Meta:
        model = Movie
        fields = ['title', 'poster', 'description', 'release_date', 'actors', 'category', 'trailer_link']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']


