from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                f'New contact form submission from {name}',
                message,
                email,
                ['youremail@example.com'],
                fail_silently=False,
            )
            return render(request, 'contact/thanks.html')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})