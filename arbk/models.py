# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class ArbkBusinesscategory(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, db_column=u'Name') # Field name made lowercase.
    class Meta:
        db_table = u'arbk_businesscategory'

class ArbkCompany(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, db_column=u'Name') # Field name made lowercase.
    regnumber = models.IntegerField(unique=True, db_column=u'RegNumber') # Field name made lowercase.
    employsnumber = models.IntegerField(db_column=u'EmploysNumber') # Field name made lowercase.
    constitutiondate = models.IntegerField(db_column=u'ConstitutionDate') # Field name made lowercase.
    telephone = models.CharField(max_length=200, db_column=u'Telephone') # Field name made lowercase.
    capital = models.TextField(db_column=u'Capital') # Field name made lowercase. This field type is a guess.
    addressstreet = models.CharField(max_length=200, db_column=u'AddressStreet') # Field name made lowercase.
    addressstreetnumber = models.CharField(max_length=10, db_column=u'AddressStreetNumber') # Field name made lowercase.
    addresscity = models.CharField(max_length=40, db_column=u'AddressCity') # Field name made lowercase.
    addresspostcode = models.CharField(max_length=10, db_column=u'AddressPostCode') # Field name made lowercase.
    primarycategory = models.ForeignKey(ArbkBusinesscategory, db_column=u'PrimaryCategory_id') # Field name made lowercase.
    class Meta:
        db_table = u'arbk_company'

class ArbkCompanyAuthorizedpersons(models.Model):
    id = models.IntegerField(primary_key=True)
    company = models.ForeignKey(ArbkCompany)
    person = models.ForeignKey(ArbkPerson)
    class Meta:
        db_table = u'arbk_company_AuthorizedPersons'

class ArbkCompanyOwners(models.Model):
    id = models.IntegerField(primary_key=True)
    company = models.ForeignKey(ArbkCompany)
    legalentity = models.ForeignKey(ArbkLegalentity)
    class Meta:
        db_table = u'arbk_company_Owners'

class ArbkCompanySecondarycategories(models.Model):
    id = models.IntegerField(primary_key=True)
    company = models.ForeignKey(ArbkCompany)
    businesscategory = models.ForeignKey(ArbkBusinesscategory)
    class Meta:
        db_table = u'arbk_company_SecondaryCategories'

class ArbkCompanycategory(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.ForeignKey(ArbkBusinesscategory, db_column=u'Category_id') # Field name made lowercase.
    class Meta:
        db_table = u'arbk_companycategory'

class ArbkLegalentity(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, db_column=u'Name') # Field name made lowercase.
    class Meta:
        db_table = u'arbk_legalentity'

class ArbkPerson(models.Model):
    id = models.IntegerField(primary_key=True)
    personalid = models.CharField(max_length=40, db_column=u'PersonalID') # Field name made lowercase.
    name = models.CharField(max_length=200, db_column=u'Name') # Field name made lowercase.
    class Meta:
        db_table = u'arbk_person'

