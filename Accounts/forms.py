# version 17 July, 2021
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
          
class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=256, )
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())



    


class UserUpload(forms.Form):
    userfile = forms.FileField(required=False)
    groupfile = forms.FileField(required=False)

