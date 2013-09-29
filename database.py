# -*- coding: utf-8 -*-

from google.appengine.ext import ndb


class User(ndb.Model):
    username = ndb.StringProperty(required=True)
    email = ndb.StringProperty()
    salt = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)


class Page(ndb.Model):
    name = ndb.StringProperty(required=True)
    content = ndb.TextProperty(required=True)
    updated = ndb.DateTimeProperty(auto_now=True)
    version = ndb.IntegerProperty(required=True)
