from django.contrib import admin
from .models import Movie
from .models import Category
from .models import Review, Rating
from .forms import RatingForm,ReviewForm
admin.site.register(Category)
admin.site.register(Movie)
class ReviewAdmin(admin.ModelAdmin):
    form = ReviewForm
    list_display = ['content']

admin.site.register(Review, ReviewAdmin)

class RatingAdmin(admin.ModelAdmin):
    form = RatingForm
    list_display = ['value']

admin.site.register(Rating, RatingAdmin)


