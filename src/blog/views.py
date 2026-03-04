from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def blog(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="blog/index.html")


def example(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="blog/example.html")
