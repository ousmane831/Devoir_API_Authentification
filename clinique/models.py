from django.db import models
from django.contrib.auth.models import AbstractUser

ROLES = [
    ('admin', 'Administrateur'),
    ('medecin', 'Médecin'),
    ('infirmier', 'Infirmier'),
    ('patient', 'Patient'),
]

class User(AbstractUser):
    role = models.CharField(max_length=20, choices=ROLES, default='patient')

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    date_naissance = models.DateField()
    adresse = models.CharField(max_length=255)

    def __str__(self):
        return self.user.get_full_name()

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medecin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, limit_choices_to={'role': 'medecin'})
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medecin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, limit_choices_to={'role': 'medecin'})
    date_rdv = models.DateTimeField()
    motif = models.CharField(max_length=255)
