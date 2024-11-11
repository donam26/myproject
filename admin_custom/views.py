from django.shortcuts import render, redirect , get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login  
from django.contrib import messages 
from django.contrib.auth.models import User 
from .models import Employee, Room, Service, Post, Offer, Comment


# Create your views here.

def admin_dashboard(request):
    return render(request, 'admin/home.html')
def admin_customer(request):
    employees = Employee.objects.all()
    return render(request, 'admin/customer.html', {'employees': employees})
def admin_employee(request):
    employees = Employee.objects.all()
    return render(request, 'admin/employee.html', {'employees': employees})
def admin_room(request):
    if request.method == 'POST':
        # Xử lý việc tạo phòng mới
        room_number = request.POST.get('room_number')
        room_type = request.POST.get('room_type')
        price_per_night = request.POST.get('price_per_night')
        status = request.POST.get('status')
        image = request.FILES.get('image')
        Room.objects.create(
            room_number=room_number,
            room_type=room_type,
            price_per_night=price_per_night,
            status=status,
            image=image
        )
        return redirect('admin_room')

    # Hiển thị danh sách phòng
    rooms = Room.objects.all()
    return render(request, 'admin/room.html', {'rooms': rooms})
    
def admin_service(request):
    if request.method == 'POST':
        # Xử lý việc tạo dịch vụ mới
        name = request.POST.get('name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        Service.objects.create(
            name=name,
            category=category,
            price=price,
            description=description,
            image=image
        )
        messages.success(request, 'Dịch vụ đã được tạo thành công.')
        return redirect('admin_service')

    # Hiển thị danh sách dịch vụ
    services = Service.objects.all()
    return render(request, 'admin/service.html', {'services': services})

def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    service.delete()
    messages.success(request, 'Dịch vụ đã được xóa thành công.')
    return redirect('admin_service')

def edit_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    if request.method == 'POST':
        service.name = request.POST.get('name')
        service.category = request.POST.get('category')
        service.price = request.POST.get('price')
        service.description = request.POST.get('description')

        if 'image' in request.FILES:
            service.image = request.FILES['image']

        service.save()
        messages.success(request, 'Dịch vụ đã được cập nhật thành công.')
        return redirect('admin_service')

    return render(request, 'admin/edit_service.html', {'service': service})
def admin_post(request):
    return render(request, 'admin/post.html')

def delete_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    room.delete()
    messages.success(request, 'Phòng đã được xóa thành công.')
    return redirect('admin_room')

def edit_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if request.method == 'POST':
        room.room_number = request.POST.get('room_number')
        room.room_type = request.POST.get('room_type')
        room.price_per_night = request.POST.get('price_per_night')
        room.status = request.POST.get('status')

        if 'image' in request.FILES:
            room.image = request.FILES['image']

        room.save()
        messages.success(request, 'Phòng đã được cập nhật thành công.')
        return redirect('admin_room')

    return render(request, 'admin/edit_room.html', {'room': room})

def admin_post(request):
    if request.method == 'POST':
        # Xử lý việc tạo bài đăng mới
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.user  # Lấy người dùng hiện tại làm tác giả
        image = request.FILES.get('image')
        Post.objects.create(
            title=title,
            content=content,
            author=author,
            image=image
        )
        messages.success(request, 'Bài đăng đã được tạo thành công.')
        return redirect('admin_post')

    # Hiển thị danh sách bài đăng
    posts = Post.objects.all()
    return render(request, 'admin/post.html', {'posts': posts})

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    messages.success(request, 'Bài đăng đã được xóa thành công.')
    return redirect('admin_post')

def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')

        if 'image' in request.FILES:
            post.image = request.FILES['image']

        post.save()
        messages.success(request, 'Bài đăng đã được cập nhật thành công.')
        return redirect('admin_post')

    return render(request, 'admin/edit_post.html', {'post': post})

def admin_gift(request):
    if request.method == 'POST':
        # Handle offer creation
        title = request.POST.get('title')
        description = request.POST.get('description')
        discount_percentage = request.POST.get('discount_percentage')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        
        Offer.objects.create(
            title=title,
            description=description,
            discount_percentage=discount_percentage,
            start_date=start_date,
            end_date=end_date
        )
        messages.success(request, 'Offer has been created successfully.')
        return redirect('admin_gift')

    # Display the list of offers
    offers = Offer.objects.all()
    return render(request, 'admin/gift.html', {'offers': offers})

def delete_gift(request, gift_id):
    offer = get_object_or_404(Offer, id=gift_id)
    offer.delete()
    messages.success(request, 'Offer has been deleted successfully.')
    return redirect('admin_gift')

def edit_gift(request, gift_id):
    offer = get_object_or_404(Offer, id=gift_id)

    if request.method == 'POST':
        offer.title = request.POST.get('title')
        offer.description = request.POST.get('description')
        offer.discount_percentage = request.POST.get('discount_percentage')
        offer.start_date = request.POST.get('start_date')
        offer.end_date = request.POST.get('end_date')

        offer.save()
        messages.success(request, 'Offer has been updated successfully.')
        return redirect('admin_gift')

    return render(request, 'admin/edit_gift.html', {'offer': offer})

