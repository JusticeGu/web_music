from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World!")

def mydate(request,year,month,day):
    return HttpResponse("the date you have input is: "+str(year)+'/'+str(month)+'/'+str(day))

def myyear(request,year):
    return render(request,'myyear.html')

def myyear_dict(request,year,month):
    return render(request,'myyear_dict.html',{'month':month})

