from django.shortcuts import render
from django.http import HttpResponse
import os

from app.charts import demo_piechart


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

        content["data"], content["labels"] = demo_piechart()

        return render(request, "index.html", content)