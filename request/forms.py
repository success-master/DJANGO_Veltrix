from django import forms
from .models import Request


class NewRequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['content', 'assign_to']



class RequestUpdateForm(forms.ModelForm):

    class Meta:
        model = Request
        fields = ['status']
