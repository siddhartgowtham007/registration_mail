from django import forms

from app.models import *

class userforms(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email']
        widgets={'password':forms.PasswordInput}

class profileforms(forms.ModelForm):
    class Meta:
        model=profile
        fields=['adress','profile_pic']