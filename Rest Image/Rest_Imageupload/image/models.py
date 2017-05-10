# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UploadImage(models.Model):
    image = models.ImageField('Image Uploaded')#Stores image uploaded

