from django.urls import path
from . import views

urlpatterns = [
    path('', views.peer_review_view, name='peer_review')
]