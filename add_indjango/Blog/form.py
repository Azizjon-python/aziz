from django.forms import forms
from .models import User

class FormClass(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'surname', 'age', 'phone']
