from django.db import models

# Create your models here.

class Post(models.Model):
  title = models.CharField('title',max_length=100)
  link = models.TextField('link')
  lang = models.TextField('lang')
  author = models.TextField('author')
  body = models.TextField('body')
  created_at = models.DateTimeField('created_at', auto_now_add=True)
  
  def __str__(self):
    return self.title