from django.db import models



class Domestic(models.Model):
        origin =models.IntegerField()
        destination = models.IntegerField()
        def clean(self):
            from django.core.exceptions import ValidationError
            if len(self.origin) <= 6:
                raise ValidationError('Enter a valid pincode')



class International(models.Model):
    Destination_country = models.CharField(max_length=100)
    origin = models.IntegerField(max_length=6)
    destination = models.IntegerField(max_length=6)


class Parcel(models.Model):
    item_weight = models.IntegerField()
    item_name = models.CharField(max_length=200)


ch = (("standard",'Standard'), ("premium",'Premium'))
sh = (("self",'Self'), ("other",'Other'))
class Services(models.Model):
    services = models.CharField(max_length=200, choices=ch)
    date = models.DateField(null=True, unique=True)
    select = models.CharField(max_length=200, choices=sh)
    image = models.ImageField(upload_to='services')
