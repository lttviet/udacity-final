# -*- coding: utf-8 -*-

from google.appengine.ext import ndb


class User(ndb.Model):
    username = ndb.StringProperty(required=True)
    email = ndb.StringProperty()
    salt = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)


class Page(ndb.Model):
    page = ndb.StringProperty(required=True)
    content = ndb.TextProperty(required=True)
    updated = ndb.DateTimeProperty(auto_now=True)


class History(ndb.Model):
    version = ndb.IntegerProperty(required=True)
    page = ndb.StringProperty(required=True)
    content = ndb.TextProperty(required=True)
    updated = ndb.DateTimeProperty(auto_now=True)
