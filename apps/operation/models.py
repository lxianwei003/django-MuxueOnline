# _*_ coding=utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from users.models import UserProfile
from courses.models import Course
'''
userAsk 用户咨询、CourseComments 用户评论、UserFavorite 用户收藏、UserMessage 用户消息、UserCourse 用户学习的课程

'''
# Create your models here.

class UserAsk(models.Model):
    name = models.CharField(max_length=20,verbose_name=u"姓名")
    mobile = models.CharField(max_length=11, verbose_name=u"手机")
    course_name = models.CharField(max_length=50,verbose_name=u"课程名称")
    add_time = models.DateTimeField(default=datetime.now)


    class Meta:
        verbose_name = u"课程咨询"
        verbose_name_plural = verbose_name


class CourseComment(models.Model):
    '''
    课程评论
    '''
    user = models.ForeignKey(UserProfile,verbose_name=u"用户")
    course = models.ForeignKey(Course,verbose_name=u"课程")
    comments = models.CharField(max_length=200,verbose_name=u"评论")


    class Meta:
        verbose_name = u"课程评论"
        verbose_name_plural = verbose_name

class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile,verbose_name=u"用户")
    # course、课程机构、讲师
    fav_id = models.IntegerField(default=0,verbose_name=u"数据ID")
    fav_type = models.IntegerField(default=0,choices=((1,u"课程"),(2,u"课程机构"),(3,"教师")),\
                                   verbose_name=u"用户收藏类型")

    class Meta:
        verbose_name = u"用户收藏"
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    # 消息发给一个人或所有人
    user = models.IntegerField(default=0,verbose_name=u"接收用户id")
    message = models.CharField(max_length=500,verbose_name=u"用户消息")
    has_read = models.BooleanField(default=False,verbose_name=u"是否已读")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"用户消息"
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    course = models.ForeignKey(Course, verbose_name=u"课程")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"用户课程"
        verbose_name_plural = verbose_name


