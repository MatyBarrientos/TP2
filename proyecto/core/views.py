from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "core/index.html")


def history(request):
    return render(request, "core/history.html")


def contact(request):
    return render(request, "core/contact.html")
