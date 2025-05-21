from rest_framework import permissions

class IsMedicalStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['medecin', 'infirmier']

class IsPatientDoctor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.medecin == request.user

class HasMedicalRecordAccess(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.role == 'admin':
            return False
        if user.role == 'medecin':
            return obj.medecin == user
        if user.role == 'infirmier':
            return True  # lecture seule
        if user.role == 'patient':
            return obj.patient.user == user
        return False
