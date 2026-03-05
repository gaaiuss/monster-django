from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from blog.data import posts


def blog(request: HttpRequest) -> HttpResponse:
    print("Blog")
    context = {
        "text": "Welcome to blog",
        "title": "Blog - ",
        "posts": posts,
    }

    return render(
        request=request,
        template_name="blog/index.html",
        context=context,
    )


def post(request: HttpRequest, post_id: int) -> HttpResponse:
    print("Blog")
    context = {
        "title": f"Post {post_id} - ",
        "posts": posts,
    }

    return render(
        request=request,
        template_name="blog/index.html",
        context=context,
    )


def example(request: HttpRequest) -> HttpResponse:
    print("Example")
    context = {"text": "Welcome to blog example", "title": "Example - "}

    return render(
        request=request,
        template_name="blog/example.html",
        context=context,
    )
