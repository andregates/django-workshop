"""Handle the participant form."""
from django.forms import ModelForm
from django import forms
from workshop.models import EventParticipant


class EventParticipantForm(ModelForm):
    """Create a event participant form to register."""

    class Meta:
        """Set attributtes as well as widgets  of the form."""

        model = EventParticipant
        fields = (
            'name',
            'email',
            'company',
            'join',
            'knowledge_level',
            'interests',
            'image',
            'other_interest'
        )

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'id': 'name',
                    'autofocus': True,
                    'required': True,
                    'class': 'form-control'}),
            'email': forms.TextInput(
                attrs={
                    'id': 'email',
                    'required': True,
                    'class': 'form-control'}),
            'company': forms.TextInput(
                attrs={
                    'id': 'company',
                    'required': True,
                    'class': 'form-control'}),
            'join': forms.CheckboxInput(
                attrs={
                    'id': 'join',
                    'title': 'Você é um colaborador JOIN?'}),
            'knowledge_level': forms.Select(
                attrs={
                    'id': 'knowledgeLevel',
                    'required': True,
                    'class': 'select2 form-control'
                }),
            'other_interest': forms.TextInput(
                attrs={'class': 'form-control'})
        }
