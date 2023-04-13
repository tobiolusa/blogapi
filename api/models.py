from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title= models.CharField(max_length=255, blank=True, default='')
    content = models.TextField(blank=True, default='')
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name="post", on_delete=models.CASCADE)
    
    def __str__(self):
            return self.titlegit 
    class Meta:
        ordering = ['created_on']
        
    
