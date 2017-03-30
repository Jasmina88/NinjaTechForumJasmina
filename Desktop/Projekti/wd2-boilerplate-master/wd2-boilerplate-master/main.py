#!/usr/bin/env python
import os
import jinja2
import webapp2
import webapp2

from crons.delete_topics_cron import DeleteTopicsCron
from handlers.base import MainHandler, AboutHandler, CookieHandler
from handlers.topics import TopicCreateHandler, TopicDetailsHandler, TopicDeleteHandler
from handlers.comments import CommentCreateHandler
from workers.email_comment_worker import EmailNewCommentWorker

app = webapp2.WSGIApplication([

webapp2.Route('/', MainHandler, name="main-page"),
webapp2.Route('/about', AboutHandler, name="about-page"),
webapp2.Route('/set-cookie', CookieHandler, name="set-cookie"),
webapp2.Route('/topic/create', TopicCreateHandler, name="topic_create"),
webapp2.Route('/topic/<topic_id:\d+>', TopicDetailsHandler, name="topic_details"),
webapp2.Route('/topic/<topic_id:\d+>/comment/add', CommentCreateHandler, name="comment_create"),
webapp2.Route('/topic/<topic_id:\d+>/delete', TopicDeleteHandler, name="topic-delete"),

webapp2.Route("/task/email-new-comment", EmailNewCommentWorker),

#CRON
webapp2.Route('/cron/delete-topics', DeleteTopicsCron, name="cron-delete-topics"),
], debug=True)
