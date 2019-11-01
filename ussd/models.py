from django.db import models

# Create your models here.
class userModel(models.Model):
    mob=models.BigIntegerField()
    message=models.CharField(max_length=200)
    Name=models.CharField(max_length=100)
    #message=models.CharField()
    dist=models.IntegerField()
    def __str__(self):
        return self.name
