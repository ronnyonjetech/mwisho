from django.db import models

# Create your models here.
class Person(models.Model):
    jina = models.CharField(max_length=30)
    ujinga= models.CharField(max_length=30)