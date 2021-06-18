from django.http.response import Http404, HttpResponse
from django.shortcuts import render, HttpResponse
from datetime import date, datetime
from car_wash_app.models import Contact
# Create your views here.
def index(request):
    context = {
        'variable' : ' this msg is come from views page hello !',
        'namee'  : "SIDDHARATHA SOAM"
    }
    return render(request,'index.html',context)
    # return HttpResponse("this is home page")

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=="POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        desc= request.POST.get('desc')
        contact = Contact(name= name , phone= phone, email= email, desc= desc , date=datetime.today())
        contact.save()

    return render(request,'contact.html')

def services(request):
    # return HttpResponse("this is services page")
    return render(request,'services.html')
def blogs(request):
        # return HttpResponse("this is services page")
    return render(request,'blogs.html')
def login(request):
    return render(request,'login.html')