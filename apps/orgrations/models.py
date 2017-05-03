# _*_ coding=utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
'''
课程机构基本信息、教师基本信息、城市基本信息
CourseOrg,Teacher、CityDict
'''
# Create your models here.


class CityDict(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"机构名称")
    desc = models.TextField(verbose_name=u"机构描述")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"所在城市"
        verbose_name_plural = verbose_name

class CourseOrg(models.Model):
    #course_num = models.CharField(default=0,verbose_name=u"课程数")
    #teacher_num = models.CharField(default=0,verbose_name=u"教师数")
    name = models.CharField(max_length=50,verbose_name=u"机构名称")
    desc = models.TextField(verbose_name=u"机构描述")
    click_nums = models.IntegerField(default=0,verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0,verbose_name=u"s=收藏数")
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name=u"封面")
    address = models.CharField(max_length=150,verbose_name=u"机构地址")
    city = models.ForeignKey(CityDict,verbose_name=u"所在城市")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"课程机构"
        verbose_name_plural = verbose_name


class Teschers(models.Model):
    org = models.ForeignKey(CourseOrg,verbose_name=u"所属机构")
    name = models.CharField(max_length=10,verbose_name=u"教师名")
    work_years = models.IntegerField(default=0,verbose_name=u"教龄")
    work_company = models.CharField(max_length=50,verbose_name=u"就职公司")
    work_postion = models.CharField(max_length=50, verbose_name=u"公司职位")
    points = models.CharField(max_length=50, verbose_name=u"教学地点")
    click_nums = models.IntegerField(default=0,verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"s=收藏数")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"教师"
        verbose_name_plural = verbose_name

