# _*_ coding:utf-8 _*_
__author__ = 'lxw'
__date__ = 2017 / 4 / 14

from django import forms
from captcha.fields import CaptchaField
'''
类的字段需要同template中定义的form的name
'''
class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})
class FindPwdForm(forms.Form):
    #html name一致
    email = forms.CharField(required=True)
    captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})