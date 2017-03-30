from handlers.base import BaseHandler
from models.comment import Comment
from google.appengine.api import memcache
from google.appengine.api import users
from models.topic import Topic


class CommentCreateHandler(BaseHandler):
    def post(self, topic_id):
        csrf_token = self.request.get("csrf_token")
        mem_token = memcache.get(key=csrf_token)  # find if this CSRF exists in memcache

        if not mem_token:  # if token does not exist in memcache, write the following message
            return self.write("You are evil attacker...")

        user = users.get_current_user()

        if not user:
            return self.write("Please login before you're allowed to post a topic.")

        text = self.request.get("comment-text")
        topic = Topic.get_by_id(int(topic_id))

        Comment.create(content=text, user=user, topic=topic)

        return self.redirect_to("topic_details", topic_id=topic.key.id())