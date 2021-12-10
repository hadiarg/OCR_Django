from typing import Text
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CustomerForm, ImageUpload, CreateUserForm
from .decorator import *
from PIL import Image
import pytesseract
from .models import *
import os
from PIL import Image
from django.conf import settings


# Create your views here.


# home, index, dashboard, about
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def home(request):
    ocr_count = Ocr_Note.objects.all().count()
    text = ""
    message = ""
    if request.method == 'POST':
        print('done1')
        form = ImageUpload(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                image = request.FILES['ocr_pic']
                image = image.name
                path = settings.MEDIA_ROOT
                pathz = path + "ocr/" + image
                # os.environ['TESSDATA_PREFIX'] = "/usr/local/share/tessdata"
                text = pytesseract.image_to_string(Image.open(pathz))
                text = text.encode("ascii", "ignore")
                text = text.decode()
                
                os.remove(pathz)                    
                
            except:
                message = "check your filename"

    context = {
        'text': text,
        'ocr_count':ocr_count,
        'message': message
    }
    return render(request, 'home.html', context)


def dashboard(request):
    customer = request.user.customer
    
    form = CustomerForm(instance=customer)
    if request.method=='POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
    context= {'form':form}
    return render(request, 'dashboard.html', context)

# login logout, register
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'login.html', context)

def loOutPage(request):
    logout(request)
    return redirect('login')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Accesswas created for'+ username)
            return redirect('login')
    context = {'form':form}
    return render(request, 'register.html',context)
