from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Subscriber


def subscribe(request):
    
    if request.method == 'POST':
        form = SubscriberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have subscribed successfully!')
            return redirect('subscribe_success') # redirect to subscribe_success view
        else:
            messages.error(request, 'There was an error in your subscription.')
    else:
        form = SubscriberForm()

    template = 'subscribers/subscribe_success.html'
    context = {
        'form': form,
       
    }

    return render(request, template, context)


def subscribe_success(request):
    return render(request, 'subscribers/subscribe_success.html')


