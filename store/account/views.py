from django.shortcuts import render, redirect
from .forms import *
from django.views import View
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMessage

# Create your views here.

class SignupView(View):
    def get(self,request):
        form = SingupForm()
        return render(request,'registration/signup.html', {'form':form})
    
    def post(self,request):
        form = SingupForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.is_active = False
            obj.save()
            send_activation_code(request, obj)
            return redirect('login')
        else:
            return render(request, 'contactus.html', {'form':form})
        

class ActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return f'{user.pk}{timestamp}'

TOKEN_GENRATOR = ActivationTokenGenerator()

def send_activation_code(request, user):
    template = 'registraion/activation_email.html'
    to = user.email
    token = TOKEN_GENRATOR.make_token(user)
    uid = user.pk