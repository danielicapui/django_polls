from django import forms
from .models import Question
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class SignUpForm(UserCreationForm):
    email=forms.EmailField(max_length=254,help_text="Requer. Digite um e-mail valido")
    class Meta:
        model=User
        fields=('username','email','password1','password2')
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
