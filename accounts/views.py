from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from orders.models import Order
from .forms import DressForm
from .forms import CategoryForm
from django.contrib import messages

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        phone = request.POST.get("phone")
        address = request.POST.get("address")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect("register")

        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        
        Profile.objects.create(
            user=user,
            phone=phone,
            address=address
        )

        messages.success(request, "Account created successfully")
        return redirect("login")

    return render(request, "register.html")


def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user_obj = User.objects.get(email=email)
            username = user_obj.username
        except User.DoesNotExist:
            messages.error(request, "Email not registered")
            return redirect("login")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid password")

    return render(request, "login.html")

def user_logout(request):
    logout(request)
    return redirect("login")

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        request.user.email = request.POST.get('email')
        request.user.save()

        profile.phone = request.POST.get('phone')
        profile.address = request.POST.get('address')
        profile.save()

        return redirect('profile')

    return render(request, 'profile.html', {'profile': profile})

@login_required
def admin_dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def add_category(request):
    form = CategoryForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('add_category')

    return render(request, 'add_category.html', {'form': form})


@login_required
def add_product(request):
    form = DressForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('add_product')

    return render(request, 'add_product.html', {'form': form})

@login_required
def view_orders(request):
    orders = Order.objects.all()
    return render(request, 'view_orders.html', {'orders': orders})

@login_required
def view_users(request):
    users = User.objects.all()
    return render(request, 'view_users.html', {'users': users})