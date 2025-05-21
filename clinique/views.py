from rest_framework import viewsets
from .models import Patient, MedicalRecord, Appointment
from .serializers import PatientSerializer, MedicalRecordSerializer, AppointmentSerializer
from .permissions import *

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get_permissions(self):
        user = self.request.user
        role = getattr(user, 'role', None)
        if role == 'admin':
            return [permissions.IsAuthenticated()]
        elif role == 'medecin':
            return [IsMedicalStaff()]
        elif hasattr(user, 'patient_profile'):
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def get_queryset(self):
        user = self.request.user
        role = getattr(user, 'role', None)

        if role == 'admin':
            return Patient.objects.all()
        elif role == 'medecin':
            return Patient.objects.filter(medicalrecord__medecin=user).distinct()
        elif hasattr(user, 'patient_profile'):
            return Patient.objects.filter(user=user)
        return Patient.objects.none()

class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer

    def get_permissions(self):
        return [HasMedicalRecordAccess()]

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
