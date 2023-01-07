from django.contrib import admin

from construction.models import User, ConstructionSite, Trellis, Job, JobUser

# Register your models here.
admin.site.register(User)
admin.site.register(ConstructionSite)
admin.site.register(Trellis)
admin.site.register(Job)
admin.site.register(JobUser)
