# -*- coding: utf-8 -*-

import webapp2

# Importing request handlers
from signup import Signup
from login import Login
from logout import Logout
from wikipage import WikiPage
from editpage import EditPage


PAGE_RE = r'(/(?:[a-zA-Z0-9_-]+/?)*)'


app = webapp2.WSGIApplication([
    ('/signup', Signup),
    ('/login', Login),
    ('/logout', Logout),
    (PAGE_RE, WikiPage),
    ('/_edit' + PAGE_RE, EditPage)
], debug=True)
