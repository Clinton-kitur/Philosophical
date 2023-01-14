from django import forms
from .models import Quote
from django.contrib.auth.forms import UserCreationForm
from .models import Admin

class AdminCreationForm(UserCreationForm):
    class Meta:
        model = Admin
        fields = UserCreationForm.Meta.fields 

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['text', 'author', 'source', ]
        
