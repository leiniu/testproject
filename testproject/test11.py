#! /usr/bin/env python
#coding=utf-8
import os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

print(MEDIA_ROOT)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
print (STATIC_ROOT)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'media'),
)
print(STATICFILES_DIRS)