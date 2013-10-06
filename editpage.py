# -*- coding: utf-8 -*-

import utils


from basehandler import BaseHandler


class EditPage(BaseHandler):
    def get(self, PAGE_RE):
        username = self.get_username()
        login = True if username else False

        if login:
            v = self.request.get('v')
            if v and v.isdigit():
                p = utils.get_page(PAGE_RE, page_id=int(v))
            else:
                p = utils.get_page(PAGE_RE)

            if p is None:
                self.error(404)
            else:
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
