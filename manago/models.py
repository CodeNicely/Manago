from __future__ import unicode_literals

from django.db import models

# Create your models here.
class client_data(models.Model):
	name=models.CharField(max_length=120)
	number=models.IntegerField(null=True)
	email=models.EmailField(null=True)
	project_id=models.CharField(max_length=20)
	project_deadline=models.CharField(max_length=60)
	username=models.CharField(max_length=40)
	password=models.CharField(max_length=40)

class temp_class(models.Model):
	name=models.CharField(max_length=20)

class admin_data(models.Model):
	username=models.CharField(max_length=10)
	password=models.CharField(max_length=10)

class developer_data(models.Model):
	name=models.CharField(max_length=120)
	number=models.IntegerField(null=True)
	email=models.EmailField(null=True)
	team_id=models.CharField(max_length=120)
	role=models.CharField(max_length=120)
	project_id=models.CharField(max_length=20)
	username=models.CharField(max_length=40)
	password=models.CharField(max_length=40)


	
