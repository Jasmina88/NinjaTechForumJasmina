#!/usr/bin/env python
import os
import jinja2
import webapp2
import webapp2
from handlers.base import MainHandler, AboutHandler, CookieHandler
from handlers.topics import TopicCreateHandler, TopicDetailsHandler
from handlers.comments import CommentCreateHandler

app = webapp2.WSGIApplication([

webapp2.Route('/', MainHandler, name="main-page"),
webapp2.Route('/about', AboutHandler, name="about-page"),
webapp2.Route('/set-cookie', CookieHandler, name="nastavi-cookie"),
webapp2.Route('/topic/create', TopicCreateHandler, name="topic_create"),
webapp2.Route('/topic/<topic_id:\d+>', TopicDetailsHandler, name="topic_details"),
webapp2.Route('/topic/<topic_id:\d+>/comment/add', CommentCreateHandler, name="comment_create"),
], debug=True)
