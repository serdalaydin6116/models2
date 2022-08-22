from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
    return HttpResponse ('Hello,Welcome')

def fscohort(request):
    return HttpResponse('Hello fscohort11')

def subfolder(request):
    return HttpResponse('Hello you are in subfolder now..')
