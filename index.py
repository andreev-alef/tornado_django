# -*- coding: utf-8 -*-

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.wsgi

import django.core.handlers.wsgi

import dj.dj.wsgi
import tornado_site.index


def main():
    django_app = tornado.wsgi.WSGIContainer(django.core.handlers.wsgi.WSGIHandler)
    fallbac_dic = {'fallback': django_app}
    tornado_app = tornado.web.Application([
        (r'/tor', tornado_site.index.IndexHandler),
        (r'/dj', tornado.web.FallbackHandler, fallbac_dic)
    ])


if __name__ == '__main__':
    main()
