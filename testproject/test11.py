#! /usr/bin/env python
#coding=utf-8
from .testapp.models import Case
dict=Case.objects.filter(prd_name_id=1).order_by(id)

for d in dict:
    print(dict.title)

