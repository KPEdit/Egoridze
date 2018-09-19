from django.shortcuts import render
from .models import *


def index(request):
    forms = Article.objects.order_by('-date')
    return render(request, "index.html", {'forms':forms})