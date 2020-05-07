from django.shortcuts import render,HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages
# Create your views here.
def index(request):
    context={
            'variable1':'ashish',
            'variable2':'rohan'
           }
    return render(request,'index.html',context)
    #return HttpResponse('this is homepage')

def about(request):
    return render(request,'about.html')
#   return HttpResponse('this is about page')
def services(request):
    return render(request,'services.html')
#    return HttpResponse('this is service page')
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name1')
        email=request.POST.get('email1')
        desc=request.POST.get('desc1')
        contact=Contact(name=name,email=email,desc=desc)
        contact.save()
        messages.success(request, 'your message has been send')
        messages.success(request, 'my message has been send')
    return render(request,'contact.html')
#    return HttpResponse('this is contact page')