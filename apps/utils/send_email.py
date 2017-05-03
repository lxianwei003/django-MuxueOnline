# _*_ coding:utf-8 _*_
__author__ = 'lxw'
__date__ = '2017/4/16 11:03'

from django.core.mail import send_mail
from users.models import EmailVerifyRecod
from random import Random
from MxOnline.settings import EMAIL_FROM

def random_str(randomlength=8):
    str = ''
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    random = Random()
    length = len(chars)-1
    for i in range(randomlength):
        str+= chars[random.randint(i,length)]
    return str

def send_register_email(email,send_type='register'):
    email_record = EmailVerifyRecod()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.type = send_type
    email_record.save()

    email_title = ''
    email_body = ''
    if send_type == 'register':
        email_title = "慕学网邮箱注册验证"
        email_body = "幕学网邮箱验证连接：http://127.0.0.1:8000/active/{0}".format(code)
        send_status = send_mail(email_title,email_body,EMAIL_FROM,[email],fail_silently=False)
        if send_status:
            pass
    elif send_type == 'forget':
        email_title = "慕学网邮箱密码重置"
        email_body = "幕学网邮箱重置连接：http://127.0.0.1:8000/reset/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email], fail_silently=False)
        if send_status:
            pass