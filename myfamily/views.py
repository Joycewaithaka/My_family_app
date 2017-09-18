from django.shortcuts import render
from django.http import HttpResponse
from .models import Myfamily



# Create your views here.
# def welcome (request):
#     return render(request,'my_family.html')
    
def myfamily(request):
     myfamily = Myfamily.objects.all()
     context = {
         'myfamily':myfamily
     }
     return render(request,'my_family.html',context)

