from django.db import models

# Create your models here.
class userModel(models.Model):
    mob=models.BigIntegerField()
    message=models.CharField(max_length=200)
    Name=models.CharField(max_length=100)
    #message=models.CharField()
    dist=models.IntegerField()
    

    class Meta:
        verbose_name = _("userModel")
        verbose_name_plural = _("userModels")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("userModel_detail", kwargs={"pk": self.pk})
