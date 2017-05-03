# _*_ coding=utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50,verbose_name=u"昵称",default="")
    birth = models.DateField(verbose_name=u"生日",null=True,blank=True)
    gender = models.CharField(max_length=20,choices=(("male",u"男"),("female",u"女")),\
                              default="female")
    address = models.CharField(max_length=20,verbose_name="地址")
    tel = models.CharField(max_length=11,verbose_name="电话")
    image = models.ImageField(upload_to="image/%Y/%m",default=u"image/default.png",max_length=100)
    #add_time = models.DateTimeField(default=datetime.now)
    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class EmailVerifyRecod(models.Model):
    '''
    邮箱验证码
    code,email,send_type("注册"，"找密码"),time
    '''
    code = models.CharField(max_length=20,verbose_name=u"验证码")
    email = models.EmailField(max_length=30,verbose_name="邮箱")
    send_type = models.CharField(max_length=20,choices=(("register",u"登陆"),("forget",u"找密码")))
    send_time = models.DateTimeField(default=datetime.now,verbose_name=u"发送时间")

    class Meta:
        verbose_name=u"邮箱验证"
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return '{0}({1})'.format(self.code,self.email)

class Banner(models.Model):
    '''
    轮播图
    title,image,url(url跳转),index(顺序),add_time（表的生成时间）
    '''
    title = models.CharField(max_length=100,default="标题",verbose_name=u"标题")
    image = models.ImageField(upload_to="banner/%Y/%m",default="image/default.png",verbose_name=u"轮播图")
    url = models.URLField(max_length=200,default="/",verbose_name=u"访问地址")
    index = models.IntegerField(default=0,verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name
