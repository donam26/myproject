from django.shortcuts import render, redirect , get_object_or_404
from admin_custom.models import Room, Post, Service

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login  
from django.contrib import messages 
from django.contrib.auth.models import User 



# Create your views here.

def get_home(request):
    return render(request, 'home.html')
def get_about(request):
    return render(request, 'about.html')
def get_event(request):
    events = Post.objects.all() 
    return render(request, 'event.html', {'events': events})
def get_room(request):
    rooms = Room.objects.all() 
    return render(request, 'room.html', {'rooms': rooms})
def get_contact(request):
    return render(request, 'contact.html')
def get_service(request):
    services = Service.objects.all() 
    return render(request, 'service.html', {'services': services})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')
        
        user = User.objects.create_user(username=username, password=password)
        user.save()
        
        login(request, user)
        messages.success(request, 'Registration successful.')
        return redirect('home') 
    
    return render(request, 'register.html')


def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return render(request, 'room_detail.html', {'room': room})
