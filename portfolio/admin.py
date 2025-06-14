from pyexpat import model
from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register([About, Education, Expereince, Project, Certification, Stack] )
class ExperienceAdmin(admin.ModelAdmin):
    pass