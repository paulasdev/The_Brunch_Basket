from django.contrib import admin
from .models import faq
from .forms import FaqEntryForm


@admin.register(faq)
class FaqAdmin(admin.ModelAdmin):
    form = FaqEntryForm