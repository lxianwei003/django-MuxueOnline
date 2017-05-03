# _*_ coding=utf-8 _*_
from __future__ import unicode_literals

from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    # 名称变为中文，__init__ 添加路径
    verbose_name = u"用户信息"
