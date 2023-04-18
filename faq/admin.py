from django.contrib import admin
from .models import Faq


class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'is_published', 'created_at')
    list_filter = ('category', 'is_published')
    search_fields = ('question', 'answer')


admin.site.register(Faq, FaqAdmin)