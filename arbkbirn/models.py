from django.db import models

# Create your models here.
class Business(models.Model):
#    ID = models.IntegerField()
    Name = models.CharField(max_length=200)

class BusinessName(models.Model):
    RegNumber = models.IntegerField()
    Owners = models.CharField(max_length=200)
    EmploysNumber = models.IntegerField()
    ConstitutionDate = models.IntegerField()
    Telephone = models.IntegerField()
    Capital = models.IntegerField()
    Name = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)

#class ConnectionTable(models.Model):

#class AuthorizedPersons(models.Model):

#class People(models.Model):
