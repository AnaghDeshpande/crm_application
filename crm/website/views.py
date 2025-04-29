from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import SignUpForm
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('home')
    
    else:
        return render(request, 'home.html', {'records' : records})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and Login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "You have registered successfully.")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look up the record
        customer_record = Record.objects.get(id=pk)
        return render(request, 'customer.html', {'customer_record': customer_record})  # we are passing customer_record to customer.html
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('home')
    


def add_record(request):
    return render(request, 'add_record.html', {})




def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_rec = Record.objects.get(id=pk)
        delete_rec.delete()
        messages.success(request, "The record has been deleted")
        return redirect('home')
    else:
        messages.success(request, "You Must Be Logged In To delete That record...")
        return redirect('home')
