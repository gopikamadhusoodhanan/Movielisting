from django.urls import path
from . import views
app_name='movie'
urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('user-logout', views.user_logout, name="user-logout"),
    path('add/', views.add_movie, name='add_movie'),
    path('edit/<int:movie_id>/', views.edit_movie, name='edit_movie'),
    path('del/<int:movie_id>/',views.delete_movie,name='delete_movie'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('navbar/',views.navbar, name='navbar'),
]