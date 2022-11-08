from django import forms
from .models import App_Users
from django.core import validators


class User_registeration(forms.ModelForm):
    First_Name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your First Name'}))
    Last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your Last Name'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'autocomplete':'off', 'placeholder':'Enter your Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Re-Enter your Password'}))
    confirm_Password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Re-Enter your Password'}))
    
    #------------------------------- Run time validation on Form side (Custom)---------------------------------------------
    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = self.cleaned_data['password']
    #     rpassword = self.cleaned_data['confirm_Password']
    #     if password != rpassword:
    #         raise forms.ValidationError("Password Does not Matched")
    class Meta:
        model = App_Users
        fields = ['First_Name','Last_name','email','password', 'confirm_Password']
    

