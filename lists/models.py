from django.db import models

# Create your models here.

# class Item(object):
#     pass

class Item(models.Model):
    # pass
    # text = models.TextField()
    text = models.TextField(default='')
