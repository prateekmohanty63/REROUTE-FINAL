from django.db import models

# Create your models here.

# class Events(models.Model):
#     name=models.CharField(max_length=100)
#     img=models.ImageField(upload_to='pics')
#     desc=models.TextField()
#     amount=models.IntegerField(default=0)

class Events(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    price=models.IntegerField()
    event_link=models.URLField('#')

    def __str__(self):
        return self.name


class gallery(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='gallery')




