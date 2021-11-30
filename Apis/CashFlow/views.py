from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
# Create your views here.
def homepage(request):
    return HttpResponse("Welcome to HomePage")
