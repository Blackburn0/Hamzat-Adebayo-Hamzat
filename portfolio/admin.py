from django.contrib import admin
from .models import About, Education, Expereince, Project, Certification
# Register your models here.

admin.site.register(About)
admin.site.register(Education)
admin.site.register(Expereince)
admin.site.register(Project)
admin.site.register(Certification)