# -*- coding: utf-8 -*-

import utils


from basehandler import BaseHandler


class WikiPage(BaseHandler):
    def get(self, PAGE_RE):
        p = utils.get_page(PAGE_RE)
        username = self.get_username()
        login = True if username else False

        if p is None:
            if login:
                content = ''    # empty content
                p = utils.create_page(PAGE_RE, content)
                self.redirect('/_edit' + PAGE_RE)
            else:
                self.response.write('This page does not exist. '
                                    'Please log in to create it.')
        else:
            self.render('/templates/wikipage.html',
                        login=login,
                        username=username,
                        page=p)
