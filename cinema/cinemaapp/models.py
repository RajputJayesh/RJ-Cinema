from django.db import models

# Create your models here.


class Post(models.Model):
    name=models.CharField(max_length=50)
    mobile_num=models.CharField(max_length=10)
    show_time=models.CharField(max_length=10)
    seat_cat=models.CharField(max_length=2)
    seat_num=models.CharField(max_length=2)
    created_on=models.DateTimeField()
