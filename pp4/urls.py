from django.urls import path
from . import views

urlpatterns = [
    path('', views.pp4_view, name='pp4')
]