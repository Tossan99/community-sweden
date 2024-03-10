from django.shortcuts import render
from django.contrib import messages


def peer_review_view(request):

    return render(
        request,
        "peer_review/peer_review.html",
    )