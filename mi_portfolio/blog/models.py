from django.db import models
import datetime

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField('blog/images')
    date = models.DateField(datetime.date.today)

