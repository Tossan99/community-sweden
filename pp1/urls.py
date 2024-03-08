from django.urls import path
from . import views

urlpatterns = [
    path('', views.pp1_view, name='pp1')
]