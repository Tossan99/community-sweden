from django.views import generic
from .models import PeerReview


class PeerReviewList(generic.ListView):
    """
    View for displaying all posts
    """
    queryset = PeerReview.objects.all()
    template_name = "peer_review/peer_review.html"