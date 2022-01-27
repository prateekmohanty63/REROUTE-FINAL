from django.db import models
from django.contrib.auth.models import User
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


# class event_reg(models.Model):
#     user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
#     event=models.ForeignKey(Events,on_delete=models.CASCADE)
#     number=models.IntegerField()
#     name=models.CharField(max_length=100)
#     phone=models.IntegerField()
#     email=models.ForeignKey('auth.User.email')



