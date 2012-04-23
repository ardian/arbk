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
        list_display = ('get_company_regnumber','get_company_name', 'get_company_telephone','get_person_name')

        def get_company_name(self, obj):
            return '%s'%(obj.company.name)

        def get_company_telephone(self, obj):
            return '%s'%(obj.company.telephone)

        def get_company_regnumber(self, obj):
            return '%s'%(obj.company.regnumber)

        def get_person_name(self, obj):
            return '%s'%(obj.person.name2)

<<<<<<< HEAD
	search_fields = ['person__name2', 'company__name','company__telephone','company__regnumber',
=======
	search_fields = ['get_person_name', 'company__name','company__telephone','company__regnumber',
>>>>>>> 1399e91498041ab10ed1d1d389357bcbe47883c9
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
