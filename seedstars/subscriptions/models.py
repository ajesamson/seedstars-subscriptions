from django.db import models


# Create your models here.
class Subscription(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
