from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.urls import path

# The browser will fill the request and the view return the response
def my_view(request: HttpRequest):
    return HttpResponse('A message to someone special')

urlpatterns = [
    path('', my_view),
    path('blog/', my_view),
    path('admin/', admin.site.urls),
]
