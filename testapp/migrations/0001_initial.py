# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-16 10:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='文章标题')),
                ('keyword', models.CharField(max_length=256, verbose_name='关键字')),
                ('content', models.TextField(blank=True, default='', verbose_name='内容')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '文章',
            },
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module', models.CharField(max_length=256, verbose_name='模块')),
                ('title', models.CharField(max_length=256, verbose_name='标题')),
                ('content', models.TextField(blank=True, default='', verbose_name='内容')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '用例',
                'verbose_name_plural': '测试用例',
            },
        ),
        migrations.CreateModel(
            name='Prd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='需求名称')),
                ('prd_url', models.CharField(default='', max_length=256, verbose_name='需求地址')),
            ],
            options={
                'verbose_name': '需求名称',
                'verbose_name_plural': '需求名称',
            },
        ),
        migrations.AddField(
            model_name='case',
            name='prd_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Prd'),
        ),
    ]
