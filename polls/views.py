from django.shortcuts import render, redirect
from .forms import SignUpForm,QuestionForm
import requests
from django.contrib.auth import login,authenticate
from rest_framework import viewsets
from .models import Question
from .serializers import QuestionSerializer
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

def index(request):
    return render(request,"votacao/index.html")
def question_create(request):
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # Enviar dados para a API
            return redirect('votacao:index')
    else:
        form = QuestionForm()
    return render(request, 'question_form.html', {'form': form})

def logins(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            senha = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=senha)
            if user:
                login(request, user)
                return redirect(reverse('votacao:index'))
    else:
        form = AuthenticationForm()
    return render(request, 'votacao/login.html', {'form': form})

def cadastro(request):
    if request.method=='POST':
        print("mdiadan")
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=raw_password)
            login(request,user)
            return redirect(reverse('votacao:index'))
    else:
        form=SignUpForm()
    return render(request,'votacao/signup2.html',{'form':form})