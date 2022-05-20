from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50,verbose_name="Title")
    category = models.CharField(max_length=50,null=True)
    description = models.CharField(max_length=100)
    img = models.CharField(max_length=240)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.created_date.strftime("%d/%m/%Y") + " " + self.title

    def get_url(self):
        return reverse('posts:post_detail', args=[self.pk])
