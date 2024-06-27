# movies/views.py
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, MovieForm, ReviewForm
from .models import Movie, Review, UserProfile

# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import UserProfile
# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, MovieForm, ReviewForm
from .models import Movie, Review, UserProfile
from .models import Movie, Review, UserProfile, Category
def home(request):
    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies})

@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    favorite_movies = user_profile.favorites.all()
    return render(request, 'profile.html', {'user_profile': user_profile, 'favorite_movies': favorite_movies})
@login_required
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.added_by = request.user
            movie.save()
            return redirect('movie_detail', movie.id)
    else:
        form = MovieForm()
    return render(request, 'add_movie.html', {'form': form})

def delete_movie(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == 'POST':
        movie.delete()
        return redirect('/')  # Or wherever you want to redirect after deletion
    return render(request, 'delete_confirm.html', {'movie': movie})

@login_required
def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'edit.html',{'form':form,'movie':movie})



def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            if not UserProfile.objects.filter(user=user).exists():
                UserProfile.objects.create(user=user)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def movie_detail(request, id):  # Note: 'id' should match the URL pattern
    movie = get_object_or_404(Movie, id=id)
    reviews = Review.objects.filter(movie=movie)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user
            review.save()
            return redirect('movie_detail', id=id)  # Redirect using 'id'
    else:
        form = ReviewForm()
    return render(request, 'movie_detail.html', {'movie': movie, 'reviews': reviews, 'form': form})



