from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Admin(models.Model):
    id = models.AutoField(primary_key = True)
    username = models.CharField(max_length=30,blank=False,unique=True)
    password = models.CharField(max_length=12,blank=False)
    class Meta:
        db_table = "adminapp_admin"
class Register(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=30, blank=False)
    address = models.CharField(max_length=30, blank=False)
    email = models.CharField(max_length=30, blank=False,unique=True)
    phno = models.CharField(max_length=30, blank=False,unique=True)
    username = models.CharField(max_length=30, blank=False,unique=True)
    password = models.CharField(max_length=30, blank=False,unique=True)
    class Meta:
        db_table = "smediaregister_table"

class Packages(models.Model):
    accountid = models.AutoField(primary_key=True)
    accountcode = models.CharField(max_length=10, blank=False)
    accounttitle = models.CharField(max_length=30, blank=False)
    accountPackage = models.CharField(max_length=30, blank=False)
    desc = models.CharField(max_length=35, blank=False)
    class Meta:
        db_table = "Package_table"

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = "Post_table"