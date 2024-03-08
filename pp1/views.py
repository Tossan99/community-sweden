from django.shortcuts import render
from django.contrib import messages


def pp1_view(request):

    return render(
        request,
        "pp1/pp1.html",
    )