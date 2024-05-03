from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from .models import Movie, Review, Rating,Category
from .forms import ReviewForm, RatingForm,MovieForm

def user_logout(request):
    auth.logout(request)
    return redirect("loginapp:index")

def navbar(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'nav.html', context)

@login_required(login_url="loginapp:my-login")
def dashboard(request):
    username = request.user.username if request.user.is_authenticated else None
    movies = Movie.objects.all()
    context = {'username': username, 'movies': movies}
    return render(request, 'dashboard.html', context)


def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    # Optionally, you can retrieve related movies for this category
    movies = category.movie_set.all()
    context = {
        'category': category,
        'movies': movies
    }
    return render(request, 'category_detail.html', context)

@login_required(login_url="my-login")
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.added_by = request.user
            movie.save()
            return redirect('movie:dashboard')
        else:
            # Print form errors for debugging
            print(form.errors)
    else:
        form = MovieForm()
    categories = Category.objects.all()  # Get all categories
    return render(request, 'add_movie.html', {'form': form, 'categories': categories})

def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.user == movie.added_by:
        if request.method == 'POST':
            form = MovieForm(request.POST, request.FILES, instance=movie)
            if form.is_valid():
                form.save()
                return redirect('movie:dashboard')
        else:
            form = MovieForm(instance=movie)
        return render(request, 'edit_movie.html', {'form': form})
    else:
        return redirect('movie:dashboard')
def delete_movie(request, movie_id):
    # Retrieve the movie object based on the provided movie ID
    movie = get_object_or_404(Movie, id=movie_id)
    # Check if the current user has permission to delete the movie
    if request.user == movie.added_by:
        # Delete the movie object
        movie.delete()
        # Redirect the user to a relevant page after the deletion
        return redirect('movie:dashboard')  # Redirect to the dashboard page or any other appropriate page
    else:
        # If the user doesn't have permission, display an error message or redirect to an error page
        return render(request, 'error.html', {'message': 'You do not have permission to delete this movie.'})


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    reviews = movie.review_set.all()
    ratings = movie.rating_set.all()

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        rating_form = RatingForm(request.POST)
        if review_form.is_valid() and rating_form.is_valid():
            review = review_form.save(commit=False)
            rating = rating_form.save(commit=False)
            if request.user.is_authenticated:  # Ensure user is logged in
                review.user = request.user
                rating.user = request.user
                review.movie = movie
                rating.movie = movie
                review.save()
                rating.save()
                return redirect('movie:movie_detail', movie_id=movie_id)
            else:
                # Handle the case where user is not logged in
                # You can redirect them to the login page or show an error message
                return redirect('login')  # Example redirect to the login page

    else:
        review_form = ReviewForm()
        rating_form = RatingForm()

    return render(request, 'movie_detail.html', {'movie': movie, 'reviews': reviews, 'ratings': ratings, 'review_form': review_form, 'rating_form': rating_form})

