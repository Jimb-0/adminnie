from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime

class Login_Model(models.Model):
    username = models.CharField(max_length=20,blank=True)
    #password = models.PasswordField()
PROP_CHOICES = (
        ('', "Property Type"),
        ('prop1', 'Apartment/Condo'),
        ('prop2', 'House'),
        ('prop3', 'Office/Retail'),
        ('prop4', 'Storage'),
)

FLIGHT_CHOICES = (
        ('', 'Flights of Stairs '),
        ('flight_1', '1 flight or less'),
        ('flight_2', '2 flights'),
        ('flight_3', '3 flights'),
        ('flight_4', '4 flights'),
        ('flight_5', '5+ flights'),
)
YON = (
        ('','Need Insurance ?'),
        ('n','No'),
        ('y','Yes'),

)
REF_LIST = (
        ('','Referral Type'),
        ('ref_1', 'Friend'),
        ('ref_2', 'Social Media'),
        ('ref_3', 'Uhaul / MovingHelp'),
        ('ref_4', 'SML / Penske'),
        ('ref_5', 'ABF'),
        ('ref_6', 'Other')
)

class Quote(models.Model):
    name = models.CharField(max_length=100,blank=True)
    email = models.EmailField()
    from_zip = models.CharField(_('From ZIP'), max_length = 5)
    to_zip = models.CharField(_('To ZIP'), max_length = 5)
    flights_from = models.CharField(max_length=10,choices=FLIGHT_CHOICES)
    flights_to = models.CharField(max_length=10,choices=FLIGHT_CHOICES)
    date = models.DateTimeField(default=datetime.now)
    from_property = models.CharField(max_length=10,choices=PROP_CHOICES)
    truck_size = models.CharField(max_length=2)
    insurance = models.CharField(max_length=2, choices=YON)
    referral = models.CharField(max_length=100,blank=True, choices=REF_LIST)
    other = models.CharField(max_length = 20,blank=True)
    reff_code = models.CharField(max_length = 20,blank=True)

class Insurance(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    from_zip = models.IntegerField()
    to_zip = models.IntegerField()
    date = models.DateField()

class Comment(models.Model):
    your_name = models.CharField(max_length=100)
    your_email = models.EmailField()
    heard = models.CharField(
    max_length=100,
    )
    comment = models.TextField()

# Create your models here.
