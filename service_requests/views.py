from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomerRegistrationForm, ServiceRequestForm
from .models import ServiceRequest
from django.utils import timezone
from django.contrib.auth import logout 
from .forms import StyledAuthenticationForm 

def register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Registration failed. Please correct the errors.')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'service_requests/register.html', {'form': form})

@login_required
def dashboard(request):
    requests = ServiceRequest.objects.filter(customer__user=request.user).order_by('-created_at')
    context = {
        'requests': requests,
        'pending_count': requests.filter(status='pending').count(),
        'resolved_count': requests.filter(status='resolved').count(),
    }
    return render(request, 'service_requests/dashboard.html', context)

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user.customer
            service_request.save()
            messages.success(request, 'Service request submitted successfully!')
            return redirect('dashboard')
    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/submit_request.html', {'form': form})

@login_required
def request_detail(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk, customer__user=request.user)
    return render(request, 'service_requests/request_detail.html', {'request': service_request})
@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('register') 

def login_view(request):
    if request.method == 'POST':
        form = StyledAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Handle login logic
            pass
    else:
        form = StyledAuthenticationForm()
    
    return render(request, 'login.html', {'form': form})