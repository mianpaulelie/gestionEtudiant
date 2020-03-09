from django import forms
from inscrire_etudiant.models import Students
class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = "__all__"