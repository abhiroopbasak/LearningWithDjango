from django.http import HttpResponse
from django.shortcuts import render
from .models import deta


def index(request):
    det1=deta()
    deta.name='User'
    deta.action='Addition'

    return render(request,'home.html',{'det':deta})

def sum(request):
  val1 = int(request.GET['num1'])
  val2 = int(request.GET['num2'])
  res=val1+val2
  return render(request,'result.html',{'res':res})
