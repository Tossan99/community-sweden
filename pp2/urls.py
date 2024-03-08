from django.urls import path
from . import views

urlpatterns = [
    path('', views.pp2_view, name='pp2')
]