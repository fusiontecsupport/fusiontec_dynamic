# # software/forms.py

from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = '__all__'

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not phone.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")
        if len(phone) < 10:
            raise forms.ValidationError("Phone number must be at least 10 digits.")
        return phone

    def clean_linkedin(self):
        linkedin = self.cleaned_data.get('linkedin')
        if linkedin and not linkedin.startswith("https://"):
            raise forms.ValidationError("LinkedIn URL must start with https://")
        return linkedin

    def clean(self):
        cleaned_data = super().clean()
        experience = cleaned_data.get('experience')
        experience_other = cleaned_data.get('experience_other')

        if experience == "Other" and not experience_other:
            self.add_error('experience_other', "Please specify your experience if you chose 'Other'.")

        return cleaned_data
