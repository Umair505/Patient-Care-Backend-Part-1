from django.contrib import admin
from .models import Doctor,Designation,AvailableTime,Specialization,Review
# Register your models here.
admin.site.register(Doctor)

class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',),}
class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',),}

admin.site.register(Specialization,SpecializationAdmin)
admin.site.register(Designation,DesignationAdmin)
admin.site.register(AvailableTime)
admin.site.register(Review)