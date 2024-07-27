from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from portapp import models
from portapp.models import Contact


def home(request):
    context = {}
    return render(request, "myApp/home.html", context)

def contact_form(request):
    if request.method == "POST":
        print('post')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, email, phone, message)

        # Validate name length
        if len(name) < 2 or len(name) > 30:
            messages.error(request, 'Length of name should be between 2 and 30 characters.')
            return render(request, "myApp/home.html")

        # Validate email length
        if len(email) < 2 or len(email) > 30:
            messages.error(request, 'Invalid email. Please try again.')
            return render(request, "myApp/home.html")

        # Validate number length (if provided)
        if phone and (len(phone) < 10 or len(phone) > 12):
            messages.error(request, 'Invalid number. Please try again.')
            return render(request, "myApp/home.html")

        # Save to database
        contact_instance = Contact(name=name, email=email, phone=phone, message=message)
        contact_instance.save()

        messages.success(request, 'Thank you for contacting me! Your message has been saved.')
        print('Data has been saved to database')

    return render(request, "myApp/home.html")
