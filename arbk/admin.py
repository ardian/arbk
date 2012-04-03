from arbk.models import BusinessCategory
from arbk.models import LegalEntity
from arbk.models import Person
from arbk.models import Company
from arbk.models import CompanyCategory

from django.contrib import admin

admin.site.register(BusinessCategory)
admin.site.register(LegalEntity)
admin.site.register(Person)
admin.site.register(Company)
admin.site.register(CompanyCategory)
