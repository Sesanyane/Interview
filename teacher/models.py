from django.db import models
from django.conf import settings


class AppointmentType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=800, blank=True, null=True)

    def __str__(self):
        return self.name


# Database creation for teacher appintment.
class Appointment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True,
                             on_delete=models.DO_NOTHING)
    date = models.CharField(max_length=50)
    time_start = models.CharField(max_length=50)
    time_end = models.CharField(max_length=50)
    appointment_with = models.CharField(max_length=50, blank=True)
    update_time = models.DateField(auto_now=True, auto_now_add=False)
    frist_time = models.DateField(auto_now=False, auto_now_add=True)
    type = models.ForeignKey(AppointmentType, on_delete=models.CASCADE)

    # show filed in admin panel
    def __str__(self):
        return self.date

    def __str__(self):
        return self.time_start

    def __str__(self):
        return selftime_end

    def __str__(self):
        return self.appointment_with
