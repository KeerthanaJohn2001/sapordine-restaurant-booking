from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import SliderImage,Menu
from .forms import TableForm


def show(request):
    x=Menu.objects.all()
    return render(request,'homepage.html',{'Menu':x})

def loginn(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    return render(request,'login.html')


def reservation(request):
    if request.method=='POST':
        form =TableForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=TableForm()
        image=SliderImage.objects.all()
        return render(request,)
    

def contact_view(request):
    # If form was submitted
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        print("Contact Form Submitted:")
        print("Name:", name)
        print("Email:", email)
        print("Subject:", subject)
        print("Message:", message)
        return render(request, 'contact.html', {'success': True})
    return render(request, 'contact.html')

