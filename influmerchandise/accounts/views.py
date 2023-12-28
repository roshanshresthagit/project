from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from .forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

class LoginView(CreateView):

    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,'accounts/login.html',{'form':form})
    
    def post(self,request,*args,**kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            user=authenticate(request,
                username=request.POST.get('username'),
                password=request.POST.get('password'),
            )
            if user is not None:
                login(request,user)
                messages.success(request, 'your are login')
                return redirect('home')
            messages.error(request,'Login Failed')
            return redirect('login')    
    

class RegisterView(CreateView):

    def get(self,request,*args,**kwargs):
        form=RegisterForm()
        return render(request,'accounts/register.html',{'form':form})
    
    def post(self,request,*args,**kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request,user)
            return redirect('home')
        return self.get(request)
    

class LogoutView(CreateView):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')