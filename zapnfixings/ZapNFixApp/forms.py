# forms.py
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
        class Meta:
                model = User
                fields = ['email', 'username', 'role', 'number', 'location', 'first_name', 'last_name']

        def clean(self):
                cleaned_data = super().clean()
                email = cleaned_data.get('email')
                username = cleaned_data.get('username')

                if User.objects.filter(email=email).exists():
                        self.add_error('email', 'This email is already taken. Please choose a different one.')

                if User.objects.filter(username=username).exists():
                        self.add_error('username', 'This username is already taken. Please choose a different one.')

                return cleaned_data

class RepairForm(forms.ModelForm):

        class Meta:
            model = Repair
            fields = ['image']