from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    roll_number = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=True)


class Post(models.Model):
    Male = 'M'
    FeMale = 'F'
    GENDER_CHOICES = (
        (Male, 'Male'),
        (FeMale, 'Female'),
    )
    username = models.CharField(max_length=20, blank=False,
                                null=False)
    text = models.TextField(blank=False, null=False)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES,
                              default=Male)
    time = models.DateTimeField(auto_now_add=True)