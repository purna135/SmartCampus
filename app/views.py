from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import IrrigationData

def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return redirect('login')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def smart_irrigation(request):
    irrigation_data = IrrigationData.objects.all().order_by('-id')[:5]
    print(irrigation_data[0].time)
    return render(request, 'irrigation.html', {"irrigation_data":irrigation_data})

@login_required
def smart_bell(request):
    return render(request, 'bells.html')

@login_required
def smart_notice_board(request):
    return render(request, 'notice_board.html')

@login_required
def smart_attendance(request):
    return render(request, 'attendance.html')

@login_required
def add(request):
    return render(request, 'form.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')
