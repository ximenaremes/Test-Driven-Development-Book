from django.db import models


# Create your models here.

# class Item(object):
#     pass

class List(models.Model):
    pass

class Item(models.Model):
    # pass
    # text = models.TextField()
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)

