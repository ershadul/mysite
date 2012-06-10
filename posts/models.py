from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=128, unique=True)
    body = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'posts'
        
    def __unicode__(self):
        return self.title
        
    
    
    
    
    
    
