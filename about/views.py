from django.shortcuts import render
from django.contrib import messages


def about_view(request):

    return render(
        request,
        "about/about.html",
    )