from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('''This is my django project''')

# Create your views here.
def home(request):
    return render(request,'home.html')