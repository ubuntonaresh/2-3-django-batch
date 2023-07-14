from django.shortcuts import render
from django.http import HttpResponse
import datetime
from hlo.models import ContactUs
# Create your views here.


def xyzz(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def showthispage(request):
    return render(request, "hlo.html")

def akjsdka(request):
    return render(request, "newpage.html")


def contactus(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")
        desc = request.POST.get("message")

        savethis = ContactUs(Name=name, Age = age, Email=email, Messgae=desc)
        
        savethis.save()


    return render(request, "contactus.html")