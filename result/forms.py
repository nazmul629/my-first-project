from django import forms
from.models import ResultInfo

class AddResultForm(forms.ModelForm):
    class Meta:
        model = ResultInfo
        fields = '__all__'


class ChakeResultForm(forms.Form):
    roll = forms.IntegerField()
    