# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-12 13:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_banner_emailverifyrecod'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': '\u8f6e\u64ad\u56fe', 'verbose_name_plural': '\u8f6e\u64ad\u56fe'},
        ),
        migrations.AddField(
            model_name='banner',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='banner',
            name='image',
            field=models.ImageField(default='image/default.png', upload_to='banner/%Y/%m', verbose_name='\u8f6e\u64ad\u56fe'),
        ),
        migrations.AddField(
            model_name='banner',
            name='index',
            field=models.IntegerField(default=0, verbose_name='\u987a\u5e8f'),
        ),
        migrations.AddField(
            model_name='banner',
            name='title',
            field=models.CharField(default='\u6807\u9898', max_length=100, verbose_name='\u6807\u9898'),
        ),
        migrations.AddField(
            model_name='banner',
            name='url',
            field=models.URLField(default='/', verbose_name='\u8bbf\u95ee\u5730\u5740'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', '\u7537'), ('female', '\u5973')], default='female', max_length=2),
        ),
    ]
