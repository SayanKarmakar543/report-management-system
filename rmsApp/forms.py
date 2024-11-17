from django import forms
from rmsApp.models import ReportDetails 

class ReportDetailsForm(forms.ModelForm):
    class Meta:
        model = ReportDetails
        fields = '__all__'