from arbkdb.models import ArbkBusinesscategory
from arbkdb.models import ArbkCompany
from arbkdb.models import ArbkCompanyAuthorizedpersons
from arbkdb.models import ArbkCompanyOwners
from arbkdb.models import ArbkCompanySecondarycategories
from arbkdb.models import ArbkLegalentity
from arbkdb.models import ArbkPerson


from django.contrib import admin

admin.site.register(ArbkBusinesscategory)
admin.site.register(ArbkCompany)
admin.site.register(ArbkCompanyAuthorizedpersons)
admin.site.register(ArbkCompanyOwners)
admin.site.register(ArbkCompanySecondarycategories)
admin.site.register(ArbkLegalentity)
admin.site.register(ArbkPerson)
