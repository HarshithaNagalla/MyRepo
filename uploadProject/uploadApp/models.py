from __future__ import unicode_literals
import MySQLdb
from django.db import models

# Create your models here.
class Files(models.Model):
    file_path_one = models.CharField(max_length=3000, blank=True, null=True)
    
