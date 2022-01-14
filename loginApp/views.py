from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm, UserProfilForm
from django.contrib.auth import login, update_session_auth_hash
from blog.models import MyUser, Blog, Comment
from django.contrib.auth.decorators import login_required
from taggit.models import Tag
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.


def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('blog')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {"form":form})

@login_required(login_url='login')
def user_update(request, slug_name):
    user = MyUser.objects.get(username=slug_name)
    if request.method == 'POST':
        form_password = PasswordChangeForm(request.user, request.POST)
        form = UserProfilForm(request.POST,request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profil', slug_name=user.username)
        if form_password.is_valid():
            user = form_password.save()
            update_session_auth_hash(request, user)
            return redirect('user_profil', slug_name=user.username)
    else:
        form = UserProfilForm(instance=user)
        form_password = PasswordChangeForm(request.user)

    return render(request, 'profil.html', {'form': form,'user1': user, 'form_password':form_password})

def userprofile(request, slug_name):
    user = MyUser.objects.get(username=slug_name)
    blogs = Blog.objects.filter(user_id__username = slug_name)
    tag = Tag.objects.all().order_by('name')[:4]
    cnt = Tag.objects.all().count()
    if cnt > 4 :
        tags = Tag.objects.all().order_by('-name')[:(cnt-4)]
    comments = Comment.objects.filter(user_id__username = slug_name)
    top = Blog.objects.all().order_by('-views')[:5]
    post = Blog.objects.all().order_by('-views')[:5]
    return render(request, 'user_profil.html', {'users':user,'blogs':blogs,'comments':comments,'tag':tag,'tags':tags,'cnt':cnt,'post':post})