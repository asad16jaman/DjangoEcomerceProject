from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):

    author=models.ForeignKey(User,related_name='post_author',on_delete=models.CASCADE)
    blog_title=models.CharField(max_length=264,verbose_name='put a title ')
    slug= models.SlugField(max_length=264,unique=True)
    blog_contant=models.TextField(verbose_name='What is your own mind ')
    blog_images=models.ImageField(upload_to='blog_images',verbose_name='Image')
    pub_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-pub_date']

    def __str__(self):
        return self.blog_title

class Comment(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='blog_comment')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_comment')
    comment=models.TextField()
    pub_date=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-pub_date']

    def __str__(self):
        return self.comment


class Liked(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='likes_blog')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='like_user')


