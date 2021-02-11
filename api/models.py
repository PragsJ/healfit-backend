from django.db import models


class Consultant(models.Model):
    name = models.CharField(max_length=32)
    org_name = models.CharField(max_length=256)
    yoe = models.IntegerField() #years of experience
    mail_id = models.CharField(max_length=32)


class UserProfile(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    height = models.FloatField()
    weight = models.FloatField()
    avgcycledays = models.IntegerField()  #(4-8)
    avgperioddays = models.IntegerField() #(27-31)
    lastperiod = models.DateField()


