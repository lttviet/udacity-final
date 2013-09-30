# -*- conding: utf-8 -*-
import os

import jinja2
import webapp2

import utils

JINJA_ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    autoescape=True)


class BaseHandler(webapp2.RequestHandler):
    def render(self, template, **kw):
        """Method render takes a template file and key-value pairs.

        It substitutes keys found in template with values in pairs.
        The resulted page is sent back to user."""
        t = JINJA_ENV.get_template(template)
        self.response.write(t.render(kw))

    def set_cookie(self, user):
        """Set user cookie in headers."""
        cookie = utils.make_cookie(user)
        self.response.headers.add_header(
            'Set-Cookie',
            'user={}; Path=/'.format(cookie))

    def logout(self):
        """Set user cookie to empty in headers."""
        self.response.headers.add_header('Set-Cookie',
                                         'user=;Path=/')

    def get_username(self):
        """Check if user has a valid cookie.
        Returns username if cookie is valid."""
        cookie = self.request.cookies.get('user')
        if cookie and utils.valid_cookie(cookie):
            username = cookie.split('|')[0]
            return username
