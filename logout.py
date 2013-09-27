# -*- coding: utf-8 -*-

from basehandler import BaseHandler


class Logout(BaseHandler):
    def get(self, pre):
        self.logout()
        self.redirect(pre)
