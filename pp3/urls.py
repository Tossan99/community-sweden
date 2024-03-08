from django.urls import path
from . import views

urlpatterns = [
    path('', views.pp3_view, name='pp3')
]