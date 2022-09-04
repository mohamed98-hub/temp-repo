from pydoc import visiblename
from tkinter import HIDDEN
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    usrn=models.CharField(max_length=25)
    psw=models.CharField(max_length=25)
    age=models.IntegerField(null=True)
    #cst_email=models.EmailField(max_length=25,null=True)


def __str__(self):
    self.usrn

