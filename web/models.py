from django.db import models

# Create your models here.



class UserInfo(models.Model):
    name = models.CharField(verbose_name="姓名",max_length=16) #varchar
    pwd = models.CharField(verbose_name="姓名",max_length=64,null=True,blank=True,default="Parav1ew!") #varchar
    age = models.IntegerField(verbose_name="年龄") #int
    email = models.CharField(verbose_name="邮箱",max_length=32) #varchar