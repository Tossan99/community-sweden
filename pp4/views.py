from django.shortcuts import render
from django.contrib import messages


def pp4_view(request):

    return render(
        request,
        "pp4/pp4.html",
    )