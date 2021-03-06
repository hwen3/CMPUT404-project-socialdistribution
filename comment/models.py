from django.db import models
from author.models import Author
from post.models import Post
from post.templatetags.post_extra import datesince

# Create your models here.


class Comment(models.Model):
    guid = models.CharField(max_length=128, unique=True)
    author = models.ForeignKey(Author)
    comment = models.TextField()
    pubDate = models.DateTimeField()
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return "comment with id %s and comment is %s" % (self.guid, self.comment)

    # TODO stringfy all of the values
    def getJsonObj(self):
        commentJson = {}
        commentJson['author'] = self.author.get_json_obj()
        commentJson['comment'] = unicode(self.comment)
        commentJson['pubDate'] = unicode(self.pubDate)
        # This is only used by us since its not possible to timesince with a
        # string in django timeplate
        commentJson['timeSince'] = datesince(commentJson['pubDate'])
        commentJson['guid'] = unicode(self.guid)
        commentJson['postId'] = unicode(self.post.guid)

        return commentJson

    @staticmethod
    def getCommentsForPost(post):
        return Comment.objects.filter(post=post)

    @staticmethod
    def removeComment(comment_id):
        Comment.objects.filter(guid=comment_id).delete()

    @staticmethod
    def removeCommentsForPost(post):
        Comment.objects.filter(post=post).delete()
