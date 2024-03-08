from django.shortcuts import render
from django.contrib import messages


def blog_view(request):

    return render(
        request,
        "blog/blog.html",
    )