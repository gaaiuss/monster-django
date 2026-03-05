from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    print("Home")

    context = {"text": "Welcome to home"}

    return render(
        request=request,
        template_name="home/index.html",
        context=context,
    )
