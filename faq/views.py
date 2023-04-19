from django.shortcuts import render, redirect
from .models import faq
from .forms import FaqEntryForm


def faq(request):
    faqs = faq.objects.all()
    form = FaqEntryForm()
    if request.method == 'POST':
        form = FaqEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faq')
    context = {
        'faqs': faqs,
        'form': form,
    }
    return render(request, 'faq/faq.html', context)

