from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer

# Create your views here.

def index(request):
    custs = Customer.objects.all()
    author = 'Claudio Nil Barua'
    #custs = "Clientes"
    context = {'Author': author, 'customers': custs}
    return render(request, "customerlist.html", context)