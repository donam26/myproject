from django.shortcuts import render, redirect , get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login  
from django.contrib import messages 
from django.contrib.auth.models import User 



# Create your views here.

def admin_dashboard(request):
    return render(request, 'admin/home.html')
