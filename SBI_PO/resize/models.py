from __future__ import unicode_literals
from django.db import models

# Create your models here.

class image_upload(models.Model):
        FirstName = models.CharField(max_length=500, blank=True, null=True)
	LastName = models.CharField(max_length=500, blank=True, null=True)
        EmailAddress = models.EmailField(max_length=50, blank=True, null=True)
        Phone = models.CharField(max_length=10, blank=True, null=True)
        path = models.ImageField(upload_to = '/home/harshitha/SBI_PO/uploadfiles/', default= '/home/harshita/SBI_PO/uploadfiles/None/no_img.jpg')

	class Meta:
		managed = True
		db_table = "image_upload"
