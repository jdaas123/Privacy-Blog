from django.urls import path
from zhauth.views import *
app_name = 'zhauth'


urlpatterns = [
    path(r'login/',userlogin,name = "login"),
    path("logout/",userlogout,name = "logout"),
    path(r'register/',register,name = "register"),
    path("send_captcha/",send_email_captcha,name = "email_captcha")
]