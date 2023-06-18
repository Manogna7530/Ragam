from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    # post=Contact.objects.all()
    return render(request,"Ragam.html")

def demo(request): 
    # if request .method=='POST':
    #     name=request.POST['name']
    #     email=request.POST['email']
    #     message=request.POST['message']
    #     image=request.FILES.get('image')
        
    #     k=Contact(name=name,email=email,message=message,image=image)
    #     k.save
    return render(request,"base.html")