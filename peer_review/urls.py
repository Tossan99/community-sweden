from django.urls import path
from . import views

urlpatterns = [
    path('', views.PeerReviewList.as_view(), name='peer_review')
]