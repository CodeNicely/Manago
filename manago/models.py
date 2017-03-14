
from __future__ import unicode_literals
import random
import string
import os

from django.db import models
from django.utils.timezone import now as timezone_now
from django.utils import timezone
# Create your models here.
def create_random_string(length=30):
    if length <= 0:
        length = 30

    symbols = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join([random.choice(symbols) for x in range(length)])


def upload_to(instance, filename):
    now = timezone_now()
    filename_base, filename_ext = os.path.splitext(filename)
    return 'my_uploads/{}_{}{}'.format(
        now.strftime("%Y/%m/%d/%Y%m%d%H%M%S"),
        create_random_string(),
        filename_ext.lower()
    )

class client_data(models.Model):
	name=models.CharField(max_length=40)
	number=models.CharField(max_length=40,null=True)
	email=models.EmailField(max_length=120,unique=True,null=True)
	project_id=models.CharField(max_length=40)
	project_deadline=models.CharField(max_length=40)
	password=models.CharField(max_length=40)


class admin_data(models.Model):
	username=models.CharField(max_length=40)
	password=models.CharField(max_length=40)


class developer_data(models.Model):
	name=models.CharField(max_length=40)
	number=models.CharField(max_length=40,null=True)
	email=models.EmailField(max_length=120,unique=True,null=True)
	team_id=models.CharField(max_length=40)
	role=models.CharField(max_length=40)
	project_id=models.CharField(max_length=40)
	password=models.CharField(max_length=40)

class Attachment(models.Model):
	devid=models.EmailField(max_length=120,null=True)
	head_text=models.CharField(max_length=600,null=True)
   	text_update = models.CharField(max_length=600)
   	file_name = models.CharField(max_length=100)
   	attachment = models.FileField(upload_to='documents/')
   	date_updated = models.DateTimeField()

