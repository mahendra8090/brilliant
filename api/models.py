from django.db import models
from accounts.models import *
from django.utils import timezone

# Create your models here.
class Exam1(models.Model):
    ques = models.CharField(max_length=200)
    ans = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200) 
    option4 = models.CharField(max_length=200) 
    time = models.DateTimeField(default=timezone.now)

class Exam2(models.Model):
    ques = models.CharField(max_length=200)
    ans = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200) 
    option4 = models.CharField(max_length=200) 
    time = models.DateTimeField(default=timezone.now)

class Exam3(models.Model):
    ques = models.CharField(max_length=200)
    ans = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200) 
    option4 = models.CharField(max_length=200) 
    time = models.DateTimeField(default=timezone.now)

class Exam4(models.Model):
    ques = models.CharField(max_length=200)
    ans = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200) 
    option4 = models.CharField(max_length=200) 
    time = models.DateTimeField(default=timezone.now)

class Exam5(models.Model):
    ques = models.CharField(max_length=200)
    ans = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200) 
    option4 = models.CharField(max_length=200) 
    time = models.DateTimeField(default=timezone.now)


class General_science(models.Model):
    ques = models.CharField(max_length=200)


class Current_affairs(models.Model):
    ques = models.CharField(max_length=200)
    

class English(models.Model):
    ques = models.CharField(max_length=200)


