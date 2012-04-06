from arbk.models import ArbkBusinesscategory
from arbk.models import ArbkCompany
from arbk.models import ArbkCompanyAuthorizedpersons
from arbk.models import ArbkCompanyOwners
from arbk.models import ArbkCompanySecondarycategories
from arbk.models import ArbkCompanycategory
from arbk.models import ArbkLegalentity
from arbk.models import ArbkPerson


from django.contrib import admin

admin.site.register(ArbkBusinesscategory)
admin.site.register(ArbkCompany)
admin.site.register(ArbkCompanyAuthorizedpersons)
admin.site.register(ArbkCompanyOwners)
admin.site.register(ArbkCompanySecondarycategories)
admin.site.register(ArbkCompanycategory)
admin.site.register(ArbkLegalentity)
admin.site.register(ArbkPerson)
