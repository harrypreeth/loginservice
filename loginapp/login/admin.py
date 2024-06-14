from django.contrib import admin
from django import forms
from django.contrib.auth.hashers import make_password
from .models import StandardUser

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = StandardUser
        fields = '__all__'

    def save(self, commit=True):
        user = super().save(commit=False)
        # Hash the password before saving the user
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class UserRegister(admin.ModelAdmin):
    form = UserRegisterForm

admin.site.register(StandardUser, UserRegister)
