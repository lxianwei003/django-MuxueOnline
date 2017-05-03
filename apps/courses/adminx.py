# _*_ coding:utf-8 _*_
__author__ = 'lxw'
__date__ = '2017/04/01'

import xadmin
from .models import Course,Lessons,Video,CourseResource

class CourseAdmin(object):
    list_display = ['name','decs','detail','degree','students_num','learn_time','fav_nums'\
                    ,'click_nums','add_time',]
    search_fields = ['name', 'decs', 'detail', 'degree', 'students_num', 'learn_time', 'fav_nums' \
        , 'click_nums',  ]
    list_filter = ['name', 'decs', 'detail', 'degree', 'students_num', 'learn_time', 'fav_nums' \
        , 'click_nums', 'add_time', ]

class LessonsAdmin(object):
    list_display = ['course','name','add_time']
    search_fields = ['course','name','add_time']
    list_filter = ['course__name','name','add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name', 'add_time']
    list_filter = ['lesson__name', 'name', 'add_time']


class CourseSourceAdmin(object):
    list_display = ['course', 'name','download', 'add_time']
    search_fields = ['course', 'name','download', 'add_time']
    list_filter = ['course', 'name', 'download','add_time']

xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lessons,LessonsAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseSourceAdmin)