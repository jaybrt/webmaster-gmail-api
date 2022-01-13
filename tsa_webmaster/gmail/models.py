from django.db import models

# Create your models here.


class userEmail(models.Model):
    email_address = models.CharField(max_length=50)
