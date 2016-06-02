# -*- coding: utf-8 -*-

import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<h1>Привет из Tornado</h1>')