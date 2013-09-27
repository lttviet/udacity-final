# -*- coding: utf-8 -*-

import re
import random
import string

from SECRET import SECRET1, SECRET2

from Crypto.Hash import SHA256, HMAC
from database import User, Page


def check_username(username):
    USER_RE = re.compile(r'^[a-zA-Z0-9_-]{3,20}$')
    return USER_RE.match(username)


def used_username(username):
    q = User.query(User.username == username)
    return q.get()


def check_password(password):
    PASSWORD_RE = re.compile(r'^.{3,20}$')
    return PASSWORD_RE.match(password)


def check_verify(password, verify):
    return password == verify


def signup_errors(username, password, verify):
    username_error = password_error = verify_error = ''

    if check_username(username) is None:
        username_error = 'Please enter a valid username'
    elif used_username(username):
        username_error = 'This username is already in use'

    if check_password(password) is None:
        password_error = 'Please enter a valid password'
    if not check_verify(password, verify):
        verify_error = 'Your passwords do not match'

    return username_error, password_error, verify_error


def make_salt():
    return ''.join([random.choice(string.ascii_letters
                                  + string.digits
                                  for i in range(16))])


def hash_password(password, salt):
    h = HMAC.new(salt, password + SECRET1, SHA256)
    return h.hexdigest()


def valid_password(password, salt, hashed):
    return hash_password(password, salt) == hashed


def make_cookie(username):
    h = HMAC.new(SECRET2, username, SHA256)
    return '{}|{}'.format(username, h.hexdigest())


def valid_cookie(cookie):
    username, hashed = cookie.split('|')
    return make_cookie(username) == cookie


def create_user(username, password, email):
    salt = make_salt()
    hashed = hash_password(password, salt)
    u = User(username=username,
             email=email,
             salt=salt,
             password=hashed)
    u.put()


def login(username, password):
    u = User.query(User.username == username).get()

    if u and valid_password(password, u.salt, u.password):
        error = ''
    else:
        error = 'Invalid login!'
    return error


def create_page(PAGE_RE, content):
    p = Page(page=PAGE_RE,
             content=content)
    p.put()


def get_page(PAGE_RE):
    p = Page.query(Page.page == PAGE_RE).get()
    return p


def update_page(PAGE_RE, content):
    p = get_page(PAGE_RE)
    p.content = content
    p.put()
