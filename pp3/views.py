from django.shortcuts import render
from django.contrib import messages


def pp3_view(request):

    return render(
        request,
        "pp3/pp3.html",
    )