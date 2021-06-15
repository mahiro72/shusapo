from django.db import models
from django.contrib.auth.models import (
    PermissionsMixin, AbstractBaseUser
)
# Create your models here.
from django.contrib.auth import get_user_model


user = get_user_model()

# Create your views here.

# class User(AbstractBaseUser, PermissionsMixin):
#     user_name = models.CharField(max_length=30,unique=True)


class Company(models.Model):
    post_user = models.ForeignKey(user, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    comment = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name+"("+str(self.post_user)+")"

    class Meta:
        ordering = ('-date',)


class SAnalysis(models.Model):
    post_user = models.ForeignKey(user, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    comment = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title+"("+str(self.post_user)+")"

    class Meta:
        ordering = ('-date',)




class IAnalysis(models.Model):
    post_user = models.ForeignKey(user, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    comment = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title+"("+str(self.post_user)+")"

    class Meta:
        ordering = ('-date',)



class ES(models.Model):
    post_user = models.ForeignKey(user, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.name+"("+str(self.post_user)+")"

    class Meta:
        ordering = ('-date',)

