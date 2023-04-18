from django.shortcuts import render
from .models import Faq


def faq(request):
    # Retrieve all published FAQs from the database
    faqs = Faq.objects.filter(is_published=True)

    context = {
        'faqs': faqs
    }

    return render(request, 'faq.html', context)
