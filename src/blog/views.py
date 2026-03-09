from django.http import Http404, HttpRequest, HttpResponse
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
    found_post: dict[str, int | str] | None = None

    for post in posts:
        if post["id"] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404

    context = {
        "title": f"{found_post['title']} - ",
        "post": found_post,
    }

    return render(
        request=request,
        template_name="blog/post.html",
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
