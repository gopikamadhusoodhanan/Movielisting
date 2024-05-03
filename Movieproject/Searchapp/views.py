# views.py in Searchapp
from django.shortcuts import render
from MovieListapp.models import Movie
from .forms import MovieSearchForm

def search(request):
    query = request.GET.get('q')
    if query:
        results = Movie.objects.filter(title__icontains=query)
    else:
        results = []
    return render(request, 'search_results.html', {'results': results, 'query': query})

