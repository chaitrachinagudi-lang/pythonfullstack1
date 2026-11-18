from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    data = {
        'name': "Sanjana",
        'age': 19,
        'department': "Bca"
    }

    marks = [100, 40, 50]

    return render(request, 'home.html', {'data': data, 'marks': marks})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')