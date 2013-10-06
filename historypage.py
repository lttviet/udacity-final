# -*- coding: utf-8 -*-

import utils


from basehandler import BaseHandler


class HistoryPage(BaseHandler):
    def get(self, PAGE_RE):
        username = self.get_username()
        login = True if username else False

        pages = utils.get_pages(PAGE_RE)
        self.render('/templates/historypage.html',
                    login=login,
                    username=username,
                    pages=pages)
