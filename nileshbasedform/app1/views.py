from django.shortcuts import render, HttpResponse
from datetime import datetime
from app1.models import Contact
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    messages.success(request, "this is a test messsage")
    return render(request, "home.html")
def about(request):
    return render(request, "about.html")
    #return HttpResponse("this is about page")
def services(request):
    return render(request, "services.html")
    #return HttpResponse("this is service page")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact=Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "your  massage has been sent!")

    return render(request, "contact.html")
def index(request):
    return render(request, "index.html")
def dashboard(request):
    return render(request, "dashboard.html")
def register(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
        else:
            form=UserCreationForm()    
    return render(request, "register.html",{'form':form})
def logout(request):
    return render(request, "logout.html")
def login(request):
    return render(request, "login.html")
    #return HttpResponse("this is contact page")

