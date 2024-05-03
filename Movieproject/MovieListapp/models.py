from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from django.utils import timezone
from django.views.generic import DetailView

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True,null=True)

    def save(self, *args, **kwargs):
        # Set slug based on name
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('category_detail', args=[ self.slug])

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_object()
        context['movies'] = Movie.objects.filter(category=category)
        return context

class Movie(models.Model):
    title = models.CharField(max_length=255)
    slug=models.CharField(max_length=100, unique=True,null=True)
    poster = models.ImageField(upload_to='poster',null=True)
    description = models.TextField()
    release_date = models.DateField()
    actors = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    trailer_link = models.URLField(max_length=360)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_category_url(self):
        return reverse('category_detail', args=[self.category.slug])

    def get_poster_url(self):
        if self.poster:
            return self.poster.url
        else:
            return None

    def __str__(self):
        return self.title


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    value = models.IntegerField(blank=True,null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} - {self.movie.title} - {self.value}'
