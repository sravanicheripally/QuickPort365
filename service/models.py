from django.db import models

# Create your models here.

class Domestic(models.Model):
        origin = models.IntegerField()
        destination = models.IntegerField()


class International(models.Model):
    Destination_country = models.CharField(max_length=100)
    origin = models.IntegerField()
    destination = models.IntegerField()


class Parcel(models.Model):
    weight = models.IntegerField()
    item_name = models.CharField(max_length=200)


ch = (("1",'Standard'), ("2",'Premium'))
sh = (("1",'Self'), ("2",'Other'))
class Services(models.Model):
    services = models.CharField(max_length=200, choices=ch)
    date = models.DateField(null=True, unique=True)
    select = models.CharField(max_length=200, choices=sh)
    image = models.ImageField()
