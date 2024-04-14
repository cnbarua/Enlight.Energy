from django.db import models

# Create your models here.

class Customer (models.Model):
    id = models.IntegerField(primary_key=True)
    cus_code = models.CharField(max_length=6, unique=True)
    name = models.CharField(max_length=32, db_index=True)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=32)
    state = models.CharField(max_length=2, db_index=True)
    zipcode = models.CharField(max_length=5, unique=True)
    phone = models.CharField(max_length=11)
