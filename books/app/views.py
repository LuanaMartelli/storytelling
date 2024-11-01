from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
import os

def index(request):

        base = os.path.dirname(__file__)

        files = {
                'test': os.path.join(base, 'static/text/test.txt'),
                'test2':os.path.join(base, 'static/text/test2.txt'),
        }

        content = {}
        for key, file_path in files.items():
                with open(file_path, 'r') as file:
                        content[key] = file.read()

        return render(request, "index.html", content)