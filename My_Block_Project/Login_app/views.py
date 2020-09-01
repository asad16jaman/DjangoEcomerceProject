from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import logout,login,authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import UserSignupform,ChangeUser,InterprofilePic

# Create your views here.

def sign_up(request):
    registration=False
    form=UserSignupform()
    if request.method=='POST':
        form=UserSignupform(request.POST)
        if form.is_valid():
            form.save()
            registration=True
    diction={
        'form':form,
        'registration':registration,
    }
    return render(request,'Login_app/signup.html',context=diction)



def mylogin(request):
    form=AuthenticationForm()
    diction={
        'form':form
    }
    if request.method=='POST':
        form=AuthenticationForm(request.POST)
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)

        if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
        else:
                diction.update({'form':form})
                return HttpResponseRedirect(reverse('Login_app:login'))
    return render(request,'Login_app/login.html',context=diction)

@login_required(login_url='/')
def logout_func(request):
    logout(request)
    return HttpResponseRedirect(reverse('Login_app:login'))

@login_required(login_url='/')
def profile(request):
    return render(request,'Login_app/profile.html',context={})

@login_required(login_url='/')
def userchange(request):
    currant_user=request.user
    form=ChangeUser(instance=currant_user)
    if request.method == 'POST':
        form=ChangeUser(request.POST,instance=currant_user)
        if form.is_valid():
            form.save()
            # form=ChangeUser(instance=currant_user)
            return HttpResponseRedirect(reverse('Login_app:profile'))
    return render(request,'Login_app/change_profile.html',context={'form':form})

@login_required(login_url='/')
def change_passwordform(request):
    current_user=request.user
    form=PasswordChangeForm(current_user)
    if request.method== 'POST':
        form=PasswordChangeForm(current_user,data=request.POST)
        if form.is_valid():
            form.save()
    return render(request,'Login_app/change_password.html',context={'form':form})

@login_required(login_url='/')
def update_pro_pic(request):
    form = InterprofilePic()
    if request.method=='POST':
        form=InterprofilePic(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=request.user
            obj.save()
            return HttpResponseRedirect(reverse('Login_app:profile'))
    return render(request,'Login_app/pro_add_pic.html',context={'form':form})

@login_required(login_url='/')
def change_pro_pic(request):
    form=InterprofilePic(instance=request.user.user_profile)
    if request.method=='POST':
        form=InterprofilePic(request.POST,request.FILES,instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Login_app:profile'))

    return render(request, 'Login_app/pro_add_pic.html', context={'form': form})


