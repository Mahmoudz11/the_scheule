from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User

class RegisterStudent(UserCreationForm):
    first_name = forms.CharField(max_length=25)
    last_name  = forms.CharField(max_length=25)
    email      = forms.EmailField()

    class Meta:
        model  = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def save(self):
        user = super(RegisterStudent, self).save(commit=False)
        user.is_student = True
        user.save()
        return user

class RegisterInstructor(UserCreationForm):
    first_name = forms.CharField(max_length=25)
    last_name  = forms.CharField(max_length=25)
    email      = forms.EmailField()

    class Meta:
        model  = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def save(self):
        user = super(RegisterStudent, self).save(commit=False)
        user.is_instructor = True
        user.save()
        return user

class RegisterCoordinator(UserCreationForm):
    first_name = forms.CharField(max_length=25)
    last_name  = forms.CharField(max_length=25)
    email      = forms.EmailField()

    class Meta:
        model  = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def save(self):
        user = super(RegisterStudent, self).save(commit=False)
        user.is_coordinator = True
        user.save()
        return user
