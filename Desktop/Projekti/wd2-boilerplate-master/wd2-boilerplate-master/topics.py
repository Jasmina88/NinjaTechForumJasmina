from google.appengine.api import users
from google.appengine.api import memcache
from handlers.base import BaseHandler
from models.topic import Topic
import uuid
from models.comment import Comment

class TopicCreateHandler(BaseHandler):

    def get(self):
        csrf_token = str(uuid.uuid4())
        memcache.add(key=csrf_token, value=True, time=600)


        params = {"csrf_token": csrf_token}

        return self.render_template("topic_create.html", params=params)

    def post(self):
        csrf_token = self.request.get("csrf_token")
        mem_token = memcache.get(key=csrf_token)  # find if this CSRF exists in memcache

        if not mem_token:  # if token does not exist in memcache, write the following message

            return self.write("You are evil attacker...")



    def post(self):
        user = users.get_current_user()
        if not user:
            return self.write("You are not registered. Please log in.")

        topic_title = self.request.get
        the_content = self.request.get

        new_topic = Topic(title=topic_title, content=the_content, author_email=user.email())
        new_topic.put()

        return self.redirect_to("topic_details", topic_id=new_topic.key.id())


class TopicDetailsHandler(BaseHandler):
        def get(self, topic_id):
            topic = Topic.get_by_id(int(topic_id))

            comments = Comment.query(Comment.topic_id == topic.key.id(), Comment.deleted == False).order(Comment.created).fetch()

            csrf_token = str(uuid.uuid4())  # convert UUID to string
            memcache.add(key=csrf_token, value=True, time=600)

            params = {"topic": topic, "comments": comments, "csrf_token": csrf_token}

            return self.render_template("topic_details.html", params=params)