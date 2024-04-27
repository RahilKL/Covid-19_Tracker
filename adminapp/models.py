from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "Signup_table"


class States(models.Model):
    states = models.CharField(max_length=100)
    cases = models.IntegerField(max_length=100)
    deaths = models.IntegerField(max_length=100)
    recovered = models.IntegerField(max_length=100)
    active = models.IntegerField(max_length=100)

    class Meta:
        db_table = "States_table"
