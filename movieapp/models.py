from django.db import models

# Create your models here.

class Movie(models.Model):
    name=models.CharField(max_length=50,null="true")
    desc=models.TextField(null="true")
    year=models.IntegerField(null="true")
    img=models.ImageField(upload_to='gallery',null="true")

    def __str__(self):
        return self.name