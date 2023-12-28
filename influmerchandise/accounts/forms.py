from django import forms 
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    username=forms.CharField(max_length=64)
    password=forms.CharField(max_length=64, widget=forms.PasswordInput())


class RegisterForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ['username','email','first_name','middle_name','last_name','password1','password2']

    # def username_clean(self):
    #     username = self.cleaned_data['username'].lower()
    #     new=CustomUser.objects.filter(username=username)
    #     if new.count():
    #         raise ValidationError('Username Already Taken')
    #     return username
    
    # def email_clean(self):
    #     email = self.cleaned_data['email'].lower()
    #     new=CustomUser.objects.filter(email=email)
    #     if new.count():
    #         raise ValidationError('Email Already Used')
    #     return email
    
    # def clean_password2(self):  
    #     password1 = self.cleaned_data['password1']  
    #     password2 = self.cleaned_data['password2']  
  
    #     if password1 and password2 and password1 != password2:  
    #         raise ValidationError("Password don't match")  
    #     return password2  
  
    # def save(self, commit = True):  
        # user = CustomUser.objects.create_user(  
        #     self.cleaned_data['username'],  
        #     self.cleaned_data['email'],  
        #     self.cleaned_data['password1']  
        # )  
        # return user  