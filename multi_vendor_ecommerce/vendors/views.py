from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Vendor

# Create your views here.

def vendor_registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            company_name = request.POST.get('company_name', '')
            vendor = Vendor(user=user, company_name=company_name)
            vendor.save()
            login(request, user)
            return redirect('/dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'vendors/vendor_registration.html', {'form' : form})

@login_required
def vendor_dashboard(request):
    # Retrieve the logged-in vendor's information
    vendor = request.user.vendor

    # You can fetch other vendor-related data here
    # For example, products associated with this vendor

    return render(request, 'vendors/vendor_dashboard.html', {'vendor' : vendor})

def vendor_logout(request):
    logout(request)
    return redirect('John Doe')



