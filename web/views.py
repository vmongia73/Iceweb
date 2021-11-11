from django.shortcuts import render, HttpResponse
from web.models import Contact
from web.models import Buy
from django.contrib import messages
# Create your views here.

def index(request):
    # return HttpResponse("this is home page")
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
    #return HttpResponse("this is about page")
def services(request):
    return render(request,'services.html')
#    return HttpResponse("this is services page")
def contact(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        state = request.POST.get('state')
        complaint = request.POST.get('complaint')
        contact = Contact(firstname=firstname, lastname=lastname, email=email, phone=phone, city=city, state=state, complaint=complaint)
        contact.save()

    return render(request,'contact.html')
#    return HttpResponse("this is contact page")
def dryfruit(request):
    return render(request,'dryfruit.html')
def cake(request):
    return render(request,'cake.html')
def bynow(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        icecreamfl = request.POST.get('icecreamfl')
        quantity = request.POST.get('quantity')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        city = request.POST.get('city')
        bynow = Buy(firstname=firstname, icecreamfl=icecreamfl, quantity=quantity, email=email, phone=phone, city=city )
        bynow.save()
        messages.success(request,'your message has been sent')
    return render(request,'bynow.html')