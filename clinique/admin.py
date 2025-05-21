from django.contrib import admin
from .models import Patient, MedicalRecord, Appointment, User
# Register your models here.

admin.site.register(Patient)
admin.site.register(MedicalRecord)
admin.site.register(Appointment)
admin.site.register(User)