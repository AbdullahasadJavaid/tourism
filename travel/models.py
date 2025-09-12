from dataclasses import field
from sqlite3 import Date
from typing import OrderedDict
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.db import models


# Create your models here.
class Registration(models.Model):
  username=models.CharField(max_length=200)
  email=models.CharField(max_length=200)
  password=models.CharField(max_length=200)
  confirmpassword=models.CharField(max_length=200)
  phone=models.CharField(max_length=200)
  def __str__(self):
      return self.username

class city (models.Model):
    name=models.CharField(max_length=150)
    description=models.TextField()
    city_image=models.ImageField(upload_to='city_images')
    def __str__(self):
      return self.name

class places (models.Model):
    place_name=models.CharField(max_length=150)
    fam_map=models.CharField(max_length=150)
    city_name=models.ForeignKey(city,on_delete=models.DO_NOTHING,related_name='name_of_city')
    place_ds=models.TextField()
    place_image=models.ImageField()
    def __str__(self):
      return self.place_name

class restaurant (models.Model):
    res_name=models.CharField(max_length=150)
    res_map=models.CharField(max_length=150)
    city_name=models.ForeignKey(city,on_delete=models.DO_NOTHING,related_name='name_city')
    res_ds=models.TextField()
    res_image=models.ImageField()
    def __str__(self):
      return self.res_name

class hotel (models.Model):
    name=models.CharField(max_length=150)
    city_name=models.ForeignKey(city,on_delete=models.DO_NOTHING,related_name='city')
    hotel_description=models.TextField()
    password=models.CharField(max_length=200)
    hotel_image=models.FileField(blank=True, null=True, upload_to='hotels')
    def __str__(self):
      return self.name

class room (models.Model):
    room_name=models.CharField(max_length=150)
    hotel_name=models.ForeignKey(hotel,on_delete=models.DO_NOTHING,related_name='hotel_name')
    room_description=models.TextField()
    room_image=models.ImageField()
    price=models.IntegerField()
    def __str__(self):
      return self.room_name

class booking(models.Model):
    hotel_name=models.ForeignKey(hotel,on_delete=models.DO_NOTHING,related_name='hotelbooking')
    username=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    check_in=models.DateField('Check_in_Date')
    check_out=models.DateField('Check_out_Date')
    members=models.IntegerField()
    total_rooms=models.IntegerField()
    vechile=models.CharField(max_length=200)
    def __str__(self):
      return self.username


class package(models.Model):
  package_name=models.CharField(max_length=150)
  hotel_name=models.ForeignKey(hotel,on_delete=models.DO_NOTHING,related_name='Package_name')
  package_description=models.TextField()
  price=models.IntegerField()
  image=models.ImageField()
  def __str__(self):
      return self.package_name

class comment(models.Model):
 text=models.TextField(max_length=500)
 cus_name=models.CharField(max_length=50)
 def __str__(self):
    return self.cus_name