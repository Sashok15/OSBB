from django.db import models
from django.contrib.auth.models import User


class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_city = models.CharField(max_length=50)
    user_street = models.CharField(max_length=50)
    user_home = models.CharField(max_length=20)
    user_flat = models.IntegerField()


class Voting(models.Model):
    voting_id = models.AutoField(primary_key=True)
    voting_thema = models.TextField()
    voting_description = models.TextField()


class Osbb(models.Model):
    osbb_id = models.AutoField(primary_key=True)
    osbb_city = models.CharField(max_length=50)
    osbb_street = models.CharField(max_length=50)
    osbb_home = models.CharField(max_length=50)
    osbb_pass = models.CharField(max_length=50)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    voting_id = models.ForeignKey(Voting, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    commemt_text = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
