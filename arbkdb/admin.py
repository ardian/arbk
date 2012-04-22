
from arbkdb.models import (ArbkBusinesscategory, ArbkCompany,
  ArbkCompanyAuthorizedpersons, ArbkCompanyOwners, ArbkCompanySecondarycategories,
  ArbkLegalentity, ArbkPerson)

from django.contrib import admin

class CompanyAdmin(admin.ModelAdmin):
    search_fields = [
        'name', 'regnumber', 'employsnumber', 'constitutiondate', 'telephone', 'capital', 'addressstreet', 'addressstreetnumber', 'addresscity', 'addresspostcode',
    ]

    list_display = ['name', 'regnumber', 'employsnumber', 'constitutiondate', 'telephone', 'capital', 'addressstreet', 'addressstreetnumber', 'addresscity', 'addresspostcode']
class PersonAdmin(admin.ModelAdmin):
	search_fields = ['name2']

class CompanyAuthorizedpersonsAdmin(admin.ModelAdmin): 
#	list_display = ['person', 'company']
	list_filter = ['person', 'company']
	search_fields = ['person__name2', 'company__name','company__telephone','company__regnumber',
	'company__addressstreet','company__addressstreetnumber', 'company__addresscity',
	'company__addresspostcode', 'company__employsnumber', 'company__constitutiondate',
	'company__capital',]

#class CompanyOwnersAdmin(admin.ModelAdmin):
#	list_display = ["company__name", "legalentity"]




admin.site.register(ArbkBusinesscategory)
admin.site.register(ArbkCompany, CompanyAdmin)
admin.site.register(ArbkCompanyAuthorizedpersons, CompanyAuthorizedpersonsAdmin)
admin.site.register(ArbkCompanyOwners)
admin.site.register(ArbkCompanySecondarycategories)
admin.site.register(ArbkLegalentity)
admin.site.register(ArbkPerson, PersonAdmin)
