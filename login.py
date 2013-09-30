# -*- coding: utf-8 -*-

import utils


from basehandler import BaseHandler


class Login(BaseHandler):
    def get(self):
        self.render('/templates/login.html')

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')

        error = utils.login(username, password)
        if not error:
            self.set_cookie(username)
            self.redirect('/')
        else:
            self.render('/templates/login.html',
                        username=username,
                        error=error)
