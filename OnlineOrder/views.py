from django.shortcuts import render, redirect
from .forms import messageform, orderform
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contacts(request):
    if request.method == 'POST':
        message_form = messageform(request.POST)
        if message_form.is_valid():
            message_form.save();
            message = True
            messages.info(request, "Thank you....we will stay in contact")
            return redirect('contacts')
        else:
            messages.info(request, "Enter valid information")
            return redirect('contacts')
    else:
        message_form = messageform()
        message = False
    return render(request, "contacts.html", {'message_form':message_form, 'message':message})

def order(request):
    if request.method == 'POST':
        order_form = orderform(request.POST)
        if order_form.is_valid():
            order_form.save();
            message = True
            messages.info(request, "Thank you...your order has been received")
            return redirect('order')
        else:
            messages.info(request, "Enter valid information")
            return redirect('order')
    else:
        order_form = orderform()
        message = False
    return render(request, "order.html", {'order_form':order_form, 'message':message})
