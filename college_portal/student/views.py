
from django.shortcuts import render
from django.http import HttpResponse
from .models import Student_table
from .forms import Studentformdata


# Home page
def home(request):
    data = {
        'name': "Soumm",
        'age': 17,
        'department': "BCA"
    }

    marks = [100, 40, 50]

    return render(request, 'home.html', {
        'data': data,
        'marks': marks
    })


# About page
def about(request):
    return render(request, 'about.html')


# Contact page
def contact(request):
    return render(request, 'contact.html')


# Normal HTML form
def forms(request):
    if request.method == "POST":
        reg_no = request.POST.get('reg_no')
        name = request.POST.get('name')
        email = request.POST.get('email')
        marks = request.POST.get('marks')
        dob = request.POST.get('dob')

        Student_table.objects.create(
            reg_no=reg_no,
            name=name,
            email=email,
            marks=marks,
            dob=dob
        )

        return HttpResponse("Saved successfully!")

    return render(request, 'studentform.html')


# Django built-in form
def Student_form_dj(request):

    if request.method == "POST":

        form = Studentformdata(request.POST)

        if form.is_valid():

            reg_no1 = form.cleaned_data['reg_no1']
            name1 = form.cleaned_data['name1']
            email1 = form.cleaned_data['email1']

            return HttpResponse("Data saved successfully!")

        else:
           return HttpResponse("invalid Data")
    else:
        form=Studentformdata()
        return render(request,'studentformdata.html',{'form':form})

  