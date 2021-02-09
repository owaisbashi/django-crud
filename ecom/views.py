from django.shortcuts import render
from ecom.models import Ids

# Create your views here.
def home(request):
    return render(request,'index.html')
def contact(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        address=request.POST.get("address")
        address2=request.POST.get("address2")
        city=request.POST.get("city")
        id=Ids(email=email,password=password,address=address,address2=address2,city=city)
        id.save()
    
    return render(request,'contact.html')