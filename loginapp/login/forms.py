from django import forms
from .models import StandardUser

class StandardUserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = StandardUser
        fields = ["username", "password"]