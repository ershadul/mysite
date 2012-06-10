from django.db import models

# Create your models here.

from posts.models import Post

class Comment(models.Model):
    post = models.ForeignKey(Post)
    name = models.CharField(max_length=255)
    message = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.name
