# _*_ coding=utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
#from users.models import UserProfile
'''
三张表：课程本身、章节、章节下的每一小节课程、课程的资源表（download）:
课程与章节是一对多的关系
course、Lesson、Video、CourseResource
'''
# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=20,verbose_name=u"课程名称")
    decs = models.CharField(max_length=100,verbose_name=u"课程简介")
    detail = models.TextField(verbose_name=u"课程详情")
    degree = models.CharField(verbose_name=u"难度",max_length=2,choices=(("cj",u"初级"),("zj",u"中级"),("gj",u"高级")))
    students_num = models.IntegerField(default=0,verbose_name=u"学生数量")
    learn_time = models.IntegerField(default=0,verbose_name=u"课程时长(分钟数)")
    #type = models.CharField(max_length=30,verbose_name=u"课程类别")
    #user = models.ForeignKey("users.UserProfile")
    #lesson = models.ForeignKey("Lessons")
    fav_nums = models.IntegerField(default=0,verbose_name=u"收藏课程数")
    images = models.ImageField(upload_to="courses/%Y/%m",verbose_name=u"封面")
    click_nums = models.IntegerField(default=0,verbose_name=u"点击数")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return self.name

class Lessons(models.Model):
    '''
    courses,name,index,videows
    '''
    course = models.ForeignKey(Course,verbose_name=u"课程")
    name = models.CharField(max_length=10,verbose_name=u"章节名")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")


    class Meta:
        verbose_name = u"章节"
        verbose_name_plural=verbose_name

class Video(models.Model):
    lesson = models.ForeignKey(Lessons,verbose_name=u"章节")
    name = models.CharField(max_length=10, verbose_name=u"视频名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural=verbose_name

class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(max_length=10, verbose_name=u"课程资源")
    download = models.FileField(upload_to="course/resource/%Y/%m",verbose_name="资源下载")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural=verbose_name