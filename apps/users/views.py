# _*_ coding=utf-8 _*_
from django.shortcuts import render

from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
#Q 支持表中数据并行查询
from django.db.models import Q
from django.views.generic.base import View
from users.models import UserProfile
from users.forms import LoginForm
from users.forms import RegisterForm
from users.forms import FindPwdForm
from users.models import EmailVerifyRecod
from utils.send_email import send_register_email

# 重载登录验证authenticate方法,在setting中设置AUTHENTICATION_BACKENDS
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None
# Create your views here.

'''
基于类的view
'''
class RegisterView(View):
    def get(self,request):
        register_form = RegisterForm()
        return render(request, "register.html", {'register_form':register_form})
    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = request.POST.get("email","")
            if UserProfile.objects.filter(email=username):
                return render(request,"register.html",{"msg":"用户已注册"})
            pass_word = request.POST.get("password", "")
            user = UserProfile()
            user.username = username
            user.email = username
            user.is_active = False
            user.password = make_password(pass_word)
            if not UserProfile.objects.filter(username=username,email=username):
                user.save()
            #邮箱认证
            send_register_email(username,"register")
            return render(request, "login.html")
        else:
            return render(request,"register.html",{"register_form":register_form})


class ActiveUserView(View):
    def get(self,request,active_code):
        all_records = EmailVerifyRecod.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
            return render(request, "login.html",)
        else:
            return render(request,'active_fail.html')


class LoginView(View):
    def get(self,request):
        return render(request, "login.html", {})
    def post(self,request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user:
                if user.is_active:
                    login(request, user)
                    return render(request, "index.html")
                else:
                    return render(request, "login.html", {"msg":"用户未激活" })
            else:
                return render(request, "login.html", {"msg": "用户名或者密码错误！"})
        else:
            return render(request, "login.html", {"login_form": login_form})

class ForgetpwdView(View):
    def get(self,request):
        forms = FindPwdForm()
        return render(request,"forgetpwd.html",{"forms":forms})
    def post(self,request):
        forms = FindPwdForm(request.POST)
        if forms.is_valid():
            user_name = request.POST.get("email","")
            user = UserProfile.objects.filter(username=user_name)
            if user:
                send_register_email(user_name,'forget')
                return render(request,"sendemail_success.html",{})
        else:
            return render(request,"forgetpwd.html",{"forms":forms})


class ResetPasswordView(View):
    def get(self,request,code):
        all_recods = EmailVerifyRecod.objects.filter(code=code)
        if all_recods:
            return render(request,"password_reset.html",{})
    def post(self,request,code):
        all_recods = EmailVerifyRecod.objects.filter(code=code)
        if all_recods:
            for record in all_recods:
                email = record.email
                password = request.POST.get("password","")
                password2 = request.POST.get("password2", "")
                if password==password2:
                    user = UserProfile.objects.get(email=email)
                    user.password = password
                    user.save()
                    return render(request,"login.html")
                else:
                    return render(request,"password_reset.html",{})


class Multiply(View):
    def get(self,request,x,y):
        x = int(x)
        y = int(y)
        result = x*y
        return render(request,{"result":result})
# # def user_login(request):
#
#     if request.method=="POST":
#         user_name = request.POST.get("username","")
#         pass_word = request.POST.get("password","")
#         user = authenticate(username=user_name,password=pass_word)
#         if user :
#             login(request,user)
#             return render(request,"index.html")
#         else:
#             return render(request,"login.html",{"msg":"用户名或者密码错误！"})
#     elif request.method=="GET":
#         return render(request,"login.html",{})
