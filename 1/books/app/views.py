from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

def home(request):

        return HttpResponse('My First Home')


def index(request):
        return render(request, "index.html")