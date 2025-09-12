from django.shortcuts import render
from django.http import Http404

def homepage(request):
    raise Http404("Page not found")

def default(req):
    return render(req,'index.html')