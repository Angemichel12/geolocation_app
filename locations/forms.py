from django import forms
from .models import Location

class PropertyRegister(forms.ModelForm):
	class Meta:
		model = Location
		fields = ['image', 'description']