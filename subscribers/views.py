from django.shortcuts import render
from django.contrib import messages
from .models import Subscriber


def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']
        subscriber = Subscriber.objects.create(
            email=email, full_name=full_name)
        subscriber.save()
        return render(request, 'subscribers/success.html')
    else:
        return render(request, 'subscribers/subscribe.html')
