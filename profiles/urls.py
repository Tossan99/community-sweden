from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles_view, name='profiles')
]