from django.db import models

class BusinessCategory(models.Model):
    Name = models.CharField(max_length=200)

class LegalEntity(models.Model):
    Name = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = "LegalEntities"

class Person(models.Model):
    PersonalID = models.CharField(max_length=40)
    Name = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = "People"

class Company(models.Model):
    Name = models.CharField(max_length=200)
    RegNumber = models.IntegerField() 
    EmploysNumber = models.IntegerField()
    ConstitutionDate = models.IntegerField()
    Telephone = models.IntegerField()
    Capital = models.IntegerField() 
    AddressStreet = models.CharField(max_length=200)
    AddressStreetNumber = models.CharField(max_length=10)
    AddressCity = models.CharField(max_length=40)
    AddressPostCode = models.CharField(max_length=10)
    Owners = models.ManyToManyField(LegalEntity)
    AuthorizedPersons = models.ManyToManyField(Person)
    PrimaryCategory = models.ForeignKey(BusinessCategory  , related_name='+' )
    SecondaryCategories = models.ManyToManyField(BusinessCategory, related_name='+')
    class Meta:
        verbose_name_plural = "Companies"

class CompanyCategory(models.Model):
    Category = models.ForeignKey(BusinessCategory)
    class Meta:
        verbose_name_plural = "CompanyCategories"
       
        
