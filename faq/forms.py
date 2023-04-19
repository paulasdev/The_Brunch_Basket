from django import forms
from .models import faq


class FaqEntryForm(forms.ModelForm):
    class Meta:
        model = faq
        fields = ('question', 'answer')