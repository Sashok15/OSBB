from django.db import models


class User(models.Model):
    user_id = models.IntegerField(max_length=20,primary_key=True)
    user_name = models.CharField(max_length=50)
    user_last_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=70)
    user_pass = models.CharField(max_length=70)
    user_city = models.CharField(max_length=50)
    user_street = models.CharField(max_length=50)
    user_home = models.CharField(max_length=20)
    user_flat = models.IntegerField(max_length=20)


class Osbb(models.Model):
    osbb_id = models.IntegerField(max_length=20, primary_key=True)
    osbb_city = models.CharField(max_length=50)
    osbb_street = models.CharField(max_length=50)
    osbb_home = models.CharField(max_length=50)
    osbb_pass = models.CharField(max_length=50)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    voiting_id = models.ForeignKey(Voiting, on_delete=models.CASCADE)


class Voiting(models.Model):
    voiting_id = models.IntegerField(max_length=20, primary_key=True)
    voiting_thema = models.TextField()
    voiting_description = models.TextField()


class Comment(models.Model):
    comment_id = models.IntegerField(max_length=20, primary_key=True)
    commemt_text = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
