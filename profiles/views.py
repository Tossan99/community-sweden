from django.shortcuts import render
from django.contrib import messages


def profiles_view(request):

    return render(
        request,
        "profiles/profiles.html",
    )