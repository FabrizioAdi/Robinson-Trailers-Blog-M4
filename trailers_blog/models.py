from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    title_tag = models.CharField(max_length=250, default="Robinson Trailers Blog")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
# Created blog post gos to post detail page 
    def get_absolute_url(self):
        #return reverse('home')
        return reverse('post-detail', args=(str(self.id)))
