from django.db import models

# Create your models here.
class CaptchaModel(models.Model):
    #邮箱
    email = models.EmailField(unique=True)
    #验证码
    captcha = models.CharField(max_length=4)
    #发送时间
    create_time = models.DateTimeField(auto_now_add=True)