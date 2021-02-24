from django.urls import path
from . import views


urlpatterns = [
        path('', views.home, name='fetchapi-home'),
        path('about/', views.about, name='fetchapi-about'),
        ]
