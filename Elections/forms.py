from django import forms
from .models import Election, Position, Candidate, Voter

# CREATE YOUR FORMS HERE

class ElectionForm(forms.ModelForm):
    class Meta:
        model = Election
        fields = ('title','description','start_date','end_date','is_active')

        widgets = {}

class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ('election', 'name','description')

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ('election','position', 'name', 'bio', 'photo')

class VoterForm(forms.Form):
    class Meta:
        model = Voter
        fields = ['election', 'full_name', 'email', 'registration_number']
