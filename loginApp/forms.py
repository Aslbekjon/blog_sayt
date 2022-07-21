from django import forms
from captcha.fields import CaptchaField

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from blog.models import MyUser

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('username', 'email', 'password1', 'password2')

class UserLoginForm(AuthenticationForm):
    captcha = CaptchaField()
    class Meta:
        model = MyUser
        fields = ('username', 'papassword1ssword1', 'captcha')

class UserProfilForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = MyUser
        fields = ('username', 'first_name', 'last_name',
                  'email', 'bio', 'location', 'birth_date',
                  'img', 'facebook_link', 'instagram_link',
                  'youtube_link', 'telegram_link', 'gitHub_link')