from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()
class tags(models.Model):
    tags = models.CharField(max_length=50)

  
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()   
    created_at = models.DateTimeField(auto_now_add=True,null=False)
    visitors_count = models.PositiveIntegerField(default=0)
    upload_time = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='tumline', null=True, blank=True)
    #slug = models.SlugField(unique=True)
    tag = models.ManyToManyField(tags)
    #high = models.ForeignKey(highlight, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.title
    
class highlight(models.Model):
    highlight = models.BooleanField(default=False, null=True,blank=True)
    post= models.ForeignKey(Post, on_delete=models.CASCADE,null=True,blank=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)


    
#class Visitor(models.Model):
    #ip_address = models.GenericIPAddressField()
    #post = models.ForeignKey(Post, on_delete=models.CASCADE)


class breakingnew(models.Model):
    title = models.CharField(max_length=255)