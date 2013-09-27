# -*- coding: utf-8 -*-

import utils


from basehandler import BaseHandler


class WikiPage(BaseHandler):
    def get(self, PAGE_RE):
        p = utils.get_page(PAGE_RE)
        if p is None:
            self.redirect('/_edit' + PAGE_RE)
        else:
            self.render('/templates/wikipage.html',
                        content=p.content)
