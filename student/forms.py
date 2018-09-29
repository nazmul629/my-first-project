from django import forms
from.models import StudentInfo

class AddStudentForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = '__all__'