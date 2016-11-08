from django import forms
from django.db import models
from django.contrib.auth.models import User
from users.models import Adhaar,Login


class FileForm(forms.Form):
    qr_file = forms.FileField()
class AdhaarForm(forms.ModelForm):
    class Meta:
        model = Adhaar
        fields = ['uid','name','gender','yob','dep','lm','loc','vtc','po','dist','state','pc','mobile']
class LoginForm(forms.ModelForm):
    class Meta:
        model=Login
        fields=['uid','pc']
        
