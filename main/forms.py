from django import forms


class ResumeCreationForm(forms.Form):
    description = forms.CharField(label='Description')


class VacancyCreationForm(forms.Form):
    description = forms.CharField(label='Description')
