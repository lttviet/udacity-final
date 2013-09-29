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
            self.response.write('Please login to edit this page.')

    def post(self):
        content = self.request.get('content')
        utils.update_page(PAGE_RE, content)
        self.go_back()
