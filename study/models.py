from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    dis = models.TextField()

    class Meta:
        verbose_name="notes"
        verbose_name_plural="notes"

class work(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    dis = models.TextField()
    due = models.DateTimeField()
    is_finished=models.BooleanField(default=False)

# class youtubecls(models.Model):
#     title = models.CharField(max_length=50)
#     channel=models.CharField(max_length=50)
#     dis = models.TextField()
#     duretion = models.tex()

class todoo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    is_finished=models.BooleanField(default=False)
