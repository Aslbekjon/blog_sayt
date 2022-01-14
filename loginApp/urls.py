from django.urls import path
from .views import user_login, signup, user_update, userprofile

urlpatterns = [
    path('login', user_login, name="login"),
    path('signup', signup, name = "signup"),
    path('profil/<slug:slug_name>', user_update, name="profil"),
    path('accounts/<slug:slug_name>',userprofile,name = 'user_profil')
]