# -*- coding: utf-8 -*-

import django.http

def Index(req):
    return django.http.HttpResponse(u'<h1>Привет из Django</h1>')