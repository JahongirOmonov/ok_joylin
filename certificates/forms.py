from django import forms
from .models import Certificate

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = [
            'certificate_id',
            'first_name',
            'last_name',
            'father_name',
            'course',
            'teacher',
            'study_start_date',
            'study_end_date',
            'certificate_given_date',
        ]

        widgets = {
            'certificate_id': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Masalan: CERT-2025-001',
                    'required': True
                }
            ),
            'first_name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'father_name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'course': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'teacher': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'study_start_date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'study_end_date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'certificate_given_date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}
            ),
        }

    def clean_id(self):
        value = self.cleaned_data.get('id')
        if not value:
            raise forms.ValidationError("Sertifikat ID majburiy!")
        return value
