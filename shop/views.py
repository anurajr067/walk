from django.shortcuts import get_object_or_404, render
from . models import *

# Create your views here.
def home(request,c_slug=None):
    c_page=None
    prodt=None
    if c_slug!=None:
        c_page=get_object_or_404(categ,slug=c_slug)
        prodt=products.objects.filter(category=c_page,available=True)
    else:

        prodt=products.objects.all().filter(available=True)
    cat=categ.objects.all()   
    return render(request,'index.html',{'pr':prodt,'ct':cat})
def prodDetails(request):
    # try:
    #     prod=products.objects.get(category__slug=c_slug,slug=product_slug)
    # except Exception as e:
    #     raise e    
    return render(request,'item.html')

