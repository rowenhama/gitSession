from django.shortcuts import render
from django.http import Http404
from .models import Registration
from .forms import RegistrationForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = str(request.POST.get('username', ''))
        password = str(request.POST.get('password', ''))
        try:
             users = Registration.objects.get(username=username)
        except Registration.DoesNotExist:
            raise Http404('Username does not exist')
            return render(request, 'login.html', {'text': "username does not exist", 'color': "red"})
        if users.password == password:
            return render(request, 'home.html')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method=='POST':
        username=str(request.POST.get('username', ''))
        fullname=str(request.POST.get('fullname', ''))
        date_of_birth=str(request.POST.get('date_of_birth', ''))
        email=str(request.POST.get('email'))
        password=str(request.POST.get('password1', ''))
        password_confirm=str(request.POST.get('password2', ''))

        if password==password_confirm:
            users = Registration(username=username,password=password_confirm, fullname=fullname, date_of_birth=date_of_birth,email=email)
            users.save()
            return render(request, 'login.html')
        else:
            raise Http404('Registration unsuccessful')
    return render(request, 'register.html')
def index(request):
    return render(request, 'index.html')
def home(request):
    return render(request,'home.html')