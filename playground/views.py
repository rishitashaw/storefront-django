from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


def calculate():
    x = 1
    y = 1
    return x+y


def say_hello(request):
    x = calculate()
    return render(request, 'hello.html')
