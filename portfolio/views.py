from django.shortcuts import redirect, render
from portfolio.models import Contact
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.user.email if request.user.is_authenticated else None
        phone = request.POST.get('num')
        message = request.POST.get('message')

        contact = Contact.objects.create(name=name, email=email, phone=phone, message=message)
        contact.save()

        messages.success(request, 'Your message has been successfully submitted.')
        return redirect('home')

    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')