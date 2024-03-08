from django.shortcuts import render
from django.contrib import messages


def pp2_view(request):

    return render(
        request,
        "pp2/pp2.html",
    )