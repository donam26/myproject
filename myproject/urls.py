from django.contrib import admin
from django.urls import path
from home import views as home
from admin_custom import views as admin_custom
from django.contrib.auth.decorators import login_required, user_passes_test

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('admin_dashboard/', admin_custom.admin_dashboard, name='admin_dashboard'), 


    path('', home.get_home, name='home'),
    path('contact', home.get_contact),
    path('about', home.get_about),
    path('event', home.get_event),
    path('room', home.get_room),
    path('room/<int:room_id>/', home.room_detail, name='room_detail'),  


    path('login/', home.user_login, name='login'),
    path('register/', home.user_register, name='register'),


]
