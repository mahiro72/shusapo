from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Company)
admin.site.register(models.IAnalysis)
admin.site.register(models.SAnalysis)
admin.site.register(models.ES)