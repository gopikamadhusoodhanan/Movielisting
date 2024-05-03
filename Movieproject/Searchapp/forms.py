# forms.py in Searchapp
from django import forms

class MovieSearchForm(forms.Form):
    query = forms.CharField(label='Search for movies', max_length=100)
