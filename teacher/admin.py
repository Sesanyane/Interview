from django.contrib import admin

# Register your models here.

from .models import Appointment, AppointmentType


class TeacherAdmin(admin.ModelAdmin):
    list_display = ["date", "time_start", "time_end", "appointment_with"]
    list_filter = ('date', 'update_time')


admin.site.register(Appointment, TeacherAdmin)
admin.site.register(AppointmentType)
