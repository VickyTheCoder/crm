from django.shortcuts import render


def default(req):
    return render(req,'index.html')