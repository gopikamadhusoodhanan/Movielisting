from django.urls import path

from . import views
app_name='loginapp'
urlpatterns = [
    path('', views.homepage, name="index"),
    path('register', views.register, name="register"),
    path('my-login', views.my_login, name="my-login"),
    path('edit-profile/',views.edit_profile, name='edit_profile'),
]
