from django import forms
from pocket.manager.models import Activity


class ActivityForm(forms.ModelForm):

    class Meta:
        model = Activity
        fields = ['name', 'amount', 'date']
