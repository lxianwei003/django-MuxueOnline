# _*_ coding:utf-8 _*_
__author__ = 'lxw'
__date__ = '2017/04/01'

import xadmin

from .models import CityDict,CourseOrg,Teschers

class CityDictAdmin(object):
    list_display = [ 'name', 'desc','add_time']
    search_fields = [ 'name','desc', ]
    list_filter = [ 'name','desc', 'add_time']

class CourseOrgAdmin(object):

    list_display = ['name', 'desc','click_nums','fav_nums','address','city', 'add_time']
    search_fields = ['name', 'desc',]
    list_filter = ['name', 'desc','click_nums','fav_nums','address','city', 'add_time']

class TeachersAdmin(object):
    list_display = ['org','name', 'work_years', 'work_company', 'work_postion', 'points',\
                    'click_nums','fav_nums', 'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_postion', 'points', \
                    'click_nums', 'fav_nums',]
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_postion', 'points', \
                     'click_nums', 'fav_nums', 'add_time']

xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teschers,TeachersAdmin)