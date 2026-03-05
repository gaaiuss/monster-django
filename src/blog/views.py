from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def blog(request: HttpRequest) -> HttpResponse:
    print("Blog")
    context = {"text": "Welcome to blog", "title": "Blog - "}

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
