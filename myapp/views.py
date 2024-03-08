from django.shortcuts import render, redirect
from .forms import ContactForm, ApplyForm
from .models import Contact, Apply

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def work(request):
    return render(request, 'work.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')

def applications(request):
    if request.method == 'POST':
        form = ApplyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('applications_success')
    else:
        form = ApplyForm()
    return render(request, 'applications.html', {'form': form})

def applications_success(request):
    return render(request, 'applications_success.html')
