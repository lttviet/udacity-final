# -*- coding: utf-8 -*-

import utils


from basehandler import BaseHandler


class EditPage(BaseHandler):
    def get(self, PAGE_RE):
        username = self.get_username()
        login = True if username else False

        if login:
            p = utils.get_page(PAGE_RE)
            self.render('/templates/editpage.html',
                        login=login,
                        username=username,
                        page=p)
        else:
            self.redirect('/login')

    def post(self, PAGE_RE):
        content = self.request.get('content')
        utils.update_page(PAGE_RE, content)
        self.redirect(PAGE_RE)
