from django.forms import forms

INCIDENT_LIVE = (
    ('0', 'Live'),
    ('1', 'Test'),
)


class IncidentForm(forms.ModelForm):
    incident_live = forms.ChoiceField(widget=forms.RadioSelect(), choices=INCIDENT_LIVE)
