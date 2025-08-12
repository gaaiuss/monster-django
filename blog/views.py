from django.http import HttpResponse

# from django.shortcuts import render


# Create your views here.
def blog(request):
    print('BLOG')
    return HttpResponse('May you death serve all beings...')
