from django.contrib import admin

# Register your models here.
from .models import Branches, Inspections, Compliances, Reports

#admin.site.register(Question)
admin.site.register(Branches)
admin.site.register(Inspections)
admin.site.register(Compliances)
admin.site.register(Reports)
