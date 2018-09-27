from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product
import datetime



# Create your views here.
def home_view(request,*args,**kwargs):
    my_context={
        'page_name':'home_view',
        'current_date':datetime.date.today(),
    }
    return render(request,'home.html',my_context)


def contact_view(request,*args,**kwargs):
    my_context={
        'page_name':'contact_view'
    }
    return render(request,'contact.html',my_context)

def producto_view(request):
    products=Product.objects.order_by('price')
    return render(request,'products.html',{'products':products})
