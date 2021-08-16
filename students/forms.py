from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    username= forms.CharField(max_length=30,required=True,help_text='required.')
    email= forms.EmailField(max_length=254,required=True,help_text='reqired. Inform a avalid email address.')
    course = forms.CharField(max_length=30,required=True,help_text='required.')
    firstname=None
    lastname= None
    
    
    class  Meta:
        model = User
        fields = ('username','email','course','password1')


        
    