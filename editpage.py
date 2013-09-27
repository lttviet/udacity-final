# -*- coding: utf-8 -*-

import utils


from basehandler import BaseHandler


class EditPage(BaseHandler):
    def get(self, PAGE_RE):
        p = utils.get_page(PAGE_RE)
        self.render('/template/editpage.html',
                    content=p.content)

    def post(self, PAGE_RE):
        content = self.request.get('content')
        utils.update_page(PAGE_RE, content)
        self.redirect(PAGE_RE)
